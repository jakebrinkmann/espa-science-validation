""" Client for EarthExplorer MachineToMachine API """

import os
import json
import getpass
from functools import partial
from functools import reduce

import requests

from scival import __location__, util


def fmt_body(data=None):
    """ Format HTTP body for PHP-server """
    return {'jsonRequest': json.dumps(data)} if data else {}


def _api(url, endpoint, data=None, verb='POST'):
    """ Send an HTTP request to an endpoint, optional message body """
    url = '{}/{}'.format(url, endpoint)
    r = getattr(requests, verb.lower())(url, data=fmt_body(data))
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


def datasetfields(url, token, dataset, **kwargs):
    return _data(_api(url, 'datasetfields', {'apiKey': token, 'datasetName': dataset}))


def add_search_field(search, value, fields):
    """ Find the field-ID of a search """
    field_matches = [f for f in fields if search in f['name']]

    if len(field_matches) > 1:
        msg = ('Search "{0}" not unique. Found: [{1}]'
               .format(search, ', '.join(f['name'] for f in field_matches)))
        raise ValueError(msg)
    elif len(field_matches) < 1:
        msg = ('Search "{0}" failed. Available: [{1}]'
               .format(search, ', '.join(f['name'] for f in field_matches)))
        raise ValueError(msg)

    field_id = int(field_matches[0]['fieldId'])
    field_name = field_matches[0]['name']
    selections = field_matches[0].get('valueList')
    mapping = {str(s['name']): str(s['value']) for s in selections}

    if mapping and value not in mapping.values():
        msg = ('Invalid value {0} not found for {1}! Found: [ {2} ]'
                .format(value, field_name,
                        ', '.join('%s: %s' % (k, v) for k, v in mapping.items())))
        raise ValueError(msg)
    return {"fieldId": field_id, "value": value}


def add_additional(url, token, dataset='ARD_TILE', **kwargs):
    """ Attempts to build a complex search based on some simple JSON input
        Example: filters = {"Path": 29, "Row": 29, "Sensor": "ETM+" }
    TODO: Add support for AND/OR/BETWEEN searches
    """
    fields = datasetfields(url, token, dataset)
    return {} if len(kwargs) < 1 else {
        'additionalCriteria': {
        "filterType": "and",
            "childFilters": [
                dict(filterType="value", **add_search_field(k, v, fields))
                for k,v in kwargs.items()
            ]
        }}


def add_temporal(start=None, end=None, **kwargs):
    """ Format a temporal search (e.g. 2017-12-31) """
    is_none = [x is None for x in (start, end)]
    if all(is_none):
        return {}
    if any(is_none):
        start, end = list(filter(None, [start, end])) * 2
    kwargs = {'start': start, 'end': end}
    fields = {'start': 'startDate', 'end': 'endDate'}
    return {
        'temporalFilter':
            dict(dateField='search_date',
                 **{fields[k]: v for k,v in kwargs.items()})
        }


def build_meta_search(**kwargs):
    funcs = {'add_': add_additional, 'temporal_': add_temporal}
    return dict([(key,d[key]) for d in [f(**{k.split(y)[1]: v for k,v in kwargs.items()
                 if k.startswith(y)}) for y,f in funcs.items()] for key in d])


def make_search(token, dataset='ARD_TILE', start=1, limit=5e4, **kwargs):
    query = {'apiKey': token, 'datasetName': dataset, "sortOrder": "ASC",
             'startingNumber': start, 'maxResults': limit}
    return dict(query, **build_meta_search(**kwargs))


def search(url, token, dataset='ARD_TILE', start=1, chunk=5e3, limit=5e4, **kwargs):
    limit = limit or slimit(url, token, **kwargs)
    chunk = min(map(int, [limit, chunk]))
    msearch = make_search(token=token, dataset=dataset, **kwargs)
    searches = [dict(msearch, startingNumber=i+1, maxResults=chunk)
                for i in range(0, int(limit), int(chunk))]
    return _data(_api(url, 'search', searches)).get('results')


def slimit(url, token, dataset='ARD_TILE', **kwargs):
    searches = [make_search(token, dataset, limit=1, **kwargs)]
    return _data(_api(url, 'search', searches))[0].get('totalHits')


def read_search(name):
    """Read saved JSON search."""
    file_search = os.path.abspath(
        os.path.join(__location__,
                     'retrieve_data/ee/searches/{0}.json'.format(*name)))
    return json.loads(open(file_search, 'r').read())


def get_ee_host(env_name):
    return {
        'ops': 'https://earthexplorer.usgs.gov/'
    }[env_name]


def create_urls(token, entity_ids):
    """Request URLs for supplied Entity Ids.

    Args:
        token (str): active machine-to-machine authentication token
        entity_ids (list): entity ids returned from search query

    """
    return []


def download_search(search_name, outdir, username, ee_env='ops'):
    """Search and download via machine-to-machine inventory interface.

    Args:
        search_name (str): name of a json predefined search
        outdir (str): path to store downloaded data
        username (str): earthexplorer username, with download approval
        ee_env (str): environment to work from (i.e. ops, tst, dev)

    """
    body = read_search(search_name)
    host = get_ee_host(ee_env)
    token = login(username,
                  getpass.getpass('EE password (%s@%s): ' % (username, host)))
    for url in create_urls(token, search(host, token, body)):
        util.download(url, os.path.join(outdir, os.path.basename(url)))
