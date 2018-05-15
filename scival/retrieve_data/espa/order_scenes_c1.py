"""Place an ESPA order for potentially multiple scenes"""

# Modified from order_scenes_c1.py written by Steve Foga on 15 Aug 2014, modified by Steven Foga on 26 Jun 2017

import os
import sys
import json
import glob

import requests

from scival.retrieve_data.espa import api_config, espa_orders_api
from scival import logger, __location__


def order_text(outdir: str) -> str:
    """
    Return a string containing the full path and filename of the text file to contain the order information
    :param outdir: The full path to the output directory, os.getcwd() by default if None is specified
    :return:
    """
    if outdir is None:
        outdir = os.getcwd()

    else:
        if not os.path.exists(outdir):
            os.makedirs(outdir)

    return outdir + os.sep + "order_{}_.txt".format(api_config.timestamp())


def load_order(order_key: str='original.test1') -> dict:
    """
    Load in a pre-constructed order by default if None is specified.  Otherwise, load the order from a .yaml file
    :param order_key: A string containing the order key, otherwise "original" will be used
    :return:
    """
    if len(order_key.split('.')) == 1:
        order_key += '.*'

    file_search = os.path.abspath(os.path.join(__location__, 'retrieve_data/espa/orders/{0}/{1}.json'
                                               .format(*order_key.split('.'))))
    files = glob.glob(file_search)
    if not len(files):
        raise IOError('File does not exist: {}'.format(file_search))

    try:
        return json.load(open(files[0]))

    except Exception as exc:
        logger.error("Problem reading file: {}".format(files[0]))
        raise


def place_order(espa_env: str, username: str, outdir: str=None, order_key: str=None):
    """
    Place the order with the appropriate ESPA environment
    :param order_key: Optionally specify a keyword pointing to a specific order
    :param outdir: Optionally specify full path to the output directory, otherwise os.getcwd() is used
    :param espa_env: The name of the ESPA environment
    :param username: ESPA username
    :return:
    """

    espa_url = espa_orders_api.get_espa_env(espa_env)

    orders = load_order(order_key)

    passwd = espa_orders_api.espa_login()

    order_length = len(orders)

    response = list()

    for i, order in enumerate(orders):

        logger.info("Requesting order %d of %d", i+1, order_length)

        r = requests.post(espa_url + api_config.api_urls["order"],
                          auth=(username, passwd),
                          json=order)

        try:
            result = r.json()
            if 'orderid' not in result:
                logger.error('Order "%s" %d/%d failed: %s', order_key, i+1, order_length, result)
                continue

            response.append(result)

        except json.decoder.JSONDecodeError:  # inherits from ValueError
            # This error seems to occur when trying to decode a None-type object
            logger.error("There was likely a problem connecting with the host.  "
                         "Check to see if ESPA is down for maintenance.")

    filename = order_text(outdir)
    logger.warning('Store ordering results: %s', filename)
    with open(filename, "a") as f:
        f.write(json.dumps(response, indent=4))
