""" Client for EarthExplorer MachineToMachine API """

import os
import json
import getpass
from functools import partial
from functools import reduce

import requests

from scival import __location__, util, logger


def fmt_body(data=None):
    """ Format HTTP body for PHP-server """
    return {'jsonRequest': json.dumps(data)} if data else {}


def _api(url, endpoint, data=None, verb='POST'):
    """ Send an HTTP request to an endpoint, optional message body """
    url = '{}/{}'.format(url, endpoint)
    logger.info('%s %s...', verb.upper(), url)
    r = getattr(requests, verb.lower())(url, data=fmt_body(data))
    logger.info(r)
    r.raise_for_status()
    return r.json()


def _data(result):
    """ Strip the response and parse for errors """
    errors = result.get('error')
    if errors:
        raise IOError('M2M returned an error: {}'.format(errors))
    return result.get('data')


def login(url, username='username', password='password', **kwargs):
    return _data(_api(url, 'login', {'username': username, 'password': password}))


def search(url, token, body):
    body = dict(apiKey=token, **body)
    return [
        x['entityId'] for x in
        _data(_api(url, 'search', body)).get('results')
    ]


def read_search(name):
    """Read saved JSON search."""
    file_search = os.path.abspath(
        os.path.join(__location__,
                     'retrieve_data/ee/searches/{0}.json'.format(name)))
    doc = filter(lambda x: '//' not in x, open(file_search, 'r').readlines())
    return json.loads('\n'.join(doc))


def get_ee_host(env_name):
    return {
        'ops': 'https://earthexplorer.usgs.gov/inventory/json/v/1.4.1'
    }[env_name]


def create_urls(url, token, dataset, entities):
    """Request URLs for supplied Entity Ids.

    Args:
        token (str): active machine-to-machine authentication token
        entity_ids (list): entity ids returned from search query

    """
    products = {
        'ARD_TILE': ['SR','TOA','BT','QA']
    }[dataset]
    body = {'apiKey': token, 'datasetName': dataset,
            'entityIds': entities, 'products': products}
    return [
        x['url'] for x in  _data(_api(url, 'download', body))
    ]


def download_search(search_name, dir_out, username, ee_env='ops'):
    """Search and download via machine-to-machine inventory interface.

    Args:
        search_name (str): name of a json predefined search
        outdir (str): path to store downloaded data
        username (str): earthexplorer username, with download approval
        ee_env (str): environment to work from (i.e. ops, tst, dev)

    """
    body = read_search(search_name)
    host = get_ee_host(ee_env)
    token = login(url=host, username=username,
                  password=getpass.getpass('EE password (%s@%s): '
                                           % (username, host)))
    for url in create_urls(host, token, body['datasetName'],
                           search(host, token, body)):
        util.download(url, os.path.join(dir_out, os.path.basename(url)
                                        .split('?')[0]))
