"""Place an ESPA order for potentially multiple scenes"""

# Modified from order_scenes_c1.py written by Steve Foga on 15 Aug 2014, modified by Steven Foga on 26 Jun 2017

import os
import sys
import json

import requests

import order_specs
import api_config
import espa_orders_api


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


def load_order(order_key: str) -> dict:
    """
    Load in a pre-constructed order by default if None is specified.  Otherwise, load the order from a .yaml file
    :param order_key: A string containing the order key, otherwise "original" will be used
    :return:
    """
    if order_key is None:
        return order_specs.orders["original"]

    else:
        try:
            return order_specs.orders[order_key]

        except KeyError:
            print("The given key: {} does not exist in the order_specs.py file.".format(order_key))

            sys.exit(1)


def place_order(espa_env: str, username: str, ssl_ver: bool=True, outdir: str=None, order: str=None):
    """
    Place the order with the appropriate ESPA environment
    :param order: Optionally specify a keyword pointing to a specific order
    :param outdir: Optionally specify full path to the output directory, otherwise os.getcwd() is used
    :param ssl_ver: Depends on testing environment, True by default
    :param espa_env: The name of the ESPA environment
    :param username: ESPA username
    :return:
    """
    passwd = espa_orders_api.espa_login()

    espa_url = espa_orders_api.get_espa_env(espa_env)

    orders = load_order(order)

    order_length = len(orders)

    response = list()

    counter = 0

    for order in orders:
        counter += 1

        print("Requesting order {} of {}".format(counter, order_length))

        r = requests.post(espa_url + api_config.api_urls["order"],
                          auth=(username, passwd),
                          json=order,
                          verify=ssl_ver)

        try:
            response.append(r.json())

        except json.decoder.JSONDecodeError:  # inherits from ValueError
            # This error seems to occur when trying to decode a None-type object
            print("\nThere was likely a problem connecting with the host.  "
                  "Check to see if ESPA is down for maintenance.")

    with open(order_text(outdir), "a") as f:
        if type(response) is dict:
            f.write(str(response) + "\n")

        else:
            for resp in response:
                f.write(str(resp) + "\n")

    return None
