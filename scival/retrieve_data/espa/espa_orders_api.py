"""Download orders using information returned from ESPA API. Creates sub-directories first by scene/product ID,
then by order note."""

# Modified from get_finished_espa_orders_api.py written by Steve Foga on 19 July 2016


import os
import ast
import getpass
import time
import datetime
from typing import Union
from pprint import pprint

import requests

import api_config


def get_time() -> datetime.datetime:
    """
    Return the current time
    :return:
    """
    return datetime.datetime.now()


def espa_login() -> str:
    """
    Get ESPA password using command-line input
    :return:
    """
    return getpass.getpass("Enter ESPA password: ")


def get_espa_env(env_in: str) -> str:
    """
    Return the URL based on the specified ESPA environment - a key to look up the URL from the
    api_config.espa_env dict
    :param env_in: ESPA environment
    :return:
    """
    return api_config.espa_env[env_in]


def check_order_status(product_id: str, base_url: str, username: str, password: str) -> Union[bool, str]:
    """
    Get information regarding whether or not an order is complete, return False if the order is incomplete
    :param product_id: The product ID
    :param base_url: ESPA URL for a specific environment
    :param username: ESPA username
    :param password: ESPA password
    :return:
    """
    r = requests.get(url=base_url + api_config.api_urls["status"] + product_id,
                     auth=(username, password))

    if "msg" in r.json():
        print("Error: order not found.")

        print("Return info: {}".format(r.json()))

        return False

    else:
        r_info = r.json()[product_id]

        prod_stat = list()

        for oid in range(len(r_info)):
            prod_stat.append(str(r.json()[product_id][oid]["status"]))

        if all(status == "complete" for status in prod_stat):
            print("Orders complete and ready to download.")

            return r.json()

        else:
            print("An error has occurred or orders have not yet finished.")

            pprint(prod_stat)

            pprint(r.json())

            return False


def retrieve_order(outdir: str, order_url: str):
    """
    Download the order
    :param outdir: Full path to the order download folder
    :param order_url: Order download URL
    :return:
    """
    order_id = order_url.split("/")[-1]

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    outfile = outdir + os.sep + order_id

    print("Initiating download...")

    t = time.time()

    resp = requests.get(order_url, stream=True)

    print(resp.status_code)

    if resp.status_code == "ordered" or resp.status_code == 200:
        print("Starting download...")

        with open(outfile, "wb") as f:
            for chunk in resp.iter_content(chunk_size=2048):
                f.write(chunk)

            if os.path.exists(outfile):
                print(os.path.getsize(outfile) / 1024 / (time.time() - t) / 1024)

    else:
        print("Could not download {}".format(order_url))

        print("Error {}".format(str(resp.status_code)))

    print("Download of {} complete.".format(order_id))

    return None


def get_orders(txt_in: str, outdir: str, username: str, espa_env: str):
    """

    :param txt_in: The full path and filename of the input txt file containing the ESPA orders
    :param outdir: The full path to the output directory where orders will download to
    :param username: ESPA user name
    :param espa_env: ESPA environment
    :return:
    """
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    passwd = espa_login()

    order_list = list()
    error_list = list()
    failed_list = list()
    failed_msg_list = list()
    misc_list = list()
    misc_err_msg = list()
    rerun_list = list()

    # Populate a new list with the orders contained in the opened file pointed to by txt_in
    with open(txt_in, "r") as txt:
        for line in txt:
            if "errors" not in line:
                # Only read in lines that are missing the keyword "errors"
                order_list.append(ast.literal_eval(line))

            else:
                # Create a list of all the lines containing the keyword "errors"
                error_list.append(ast.literal_eval(line))

    # pprint(order_list)
    # pprint(error_list)

    t0 = get_time()

    espa_url = get_espa_env(espa_env)

    for order in order_list:

        if order["status"] == "failed" or order["status"] == 400:
            failed_list.append(order)

            failed_msg_list.append(order["message"])

        elif order["status"] == "ordered" or order["status"] == 200:
            print("Getting order ID...")

            order_info = check_order_status(order[u"orderid"], espa_url, username, passwd)

            # print(order_info)

            if order_info is not False:
                status_info = order_info[order[u"orderid"]]

                scene_id = list()
                dl_url = list()

                order_info = requests.get(espa_url + api_config.api_urls["order"] + order[u"orderid"],
                                          auth=(username, passwd))

                note = str(order_info.json()["product_opts"]["note"].capitalize())

                for j in status_info:
                    j = dict(j)

                    scene_id.append(j["name"])

                    dl_url.append(j["product_dload_url"])

                if len(scene_id) > 2:
                    ord_sid = "multiple_" + scene_id[0]

                elif len(scene_id) > 1:
                    sid_sort = sorted(scene_id)

                    ord_sid = sid_sort[0] + "_" + sid_sort[1]

                else:
                    ord_sid = scene_id[0]

                for url in dl_url:
                    output_dir = outdir + os.sep + ord_sid + os.sep + note

                    retrieve_order(output_dir, url)

            else:
                print("Could not retrieve order {}.".format(order[u"orderid"]))

                misc_list.append("Could not download order.")

                misc_err_msg.append("Could not download order.")

                rerun_list.append(order)

        else:
            misc_list.append(order["status"])

            try:
                misc_err_msg.append(order["message"])
            except KeyError:
                pass

    print("Error orders (400): {}".format(failed_list))
    print("Why orders failed: {}".format(failed_msg_list))

    print("Orders not yet finished: {}".format(rerun_list))

    print("Other error statuses: {}".format(misc_list))
    print("Why other errors happened: {}".format(misc_err_msg))

    if len(rerun_list) > 0:

        re_out = outdir + os.sep + "rerun_{}_.txt".format(api_config.timestamp())

        print("Writing unfinished order list to {}".format(re_out))

        with open(re_out, "w") as t:
            for line in rerun_list:
                t.write(str(line) + "\n")

    t1 = get_time()

    print("Processing time: {}".format(t1 - t0))

    return None
