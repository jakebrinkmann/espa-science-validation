""" Utilities for host system interaction """

import os
import time
import sys
import logging
import datetime

import urllib3
import requests

from . import logger
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def setup_logger(verbosity, stream='stderr'):
    """ configure logging via verbosity level of between 0 and 2 corresponding
    to log levels warning, info and debug respectfully. """
    global logger

    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log_out = "log_{0:%Y%m%d-%H%M%S}.log".format(datetime.datetime.now())
    fh = logging.FileHandler(log_out)
    fh.setFormatter(log_formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    log_level = max(logging.DEBUG, logging.WARNING - logging.DEBUG*verbosity)
    ch = logging.StreamHandler(stream=getattr(sys, stream.lower()))
    ch.setFormatter(log_formatter)
    ch.setLevel(log_level)
    logger.addHandler(ch)
    logger.setLevel(log_level)


def download(url: str, outfile: str):
    """Download the order.

    :param order_url: Order download URL
    :param outdir: Full path to the order download folder
    :return:
    """

    if os.path.exists(outfile):
        logger.warning("File already exists: %s", outfile)
        return

    outdir = os.path.dirname(outfile)
    if not os.path.exists(outdir):
        logger.warning("Create directory %s", outdir)
        os.makedirs(outdir)

    start = time.time()
    logger.info('Download %s', url)
    resp = requests.get(url, timeout=3,
                        stream=True, verify=False,
                        allow_redirects=True)

    try:
        bytes_in_mb = 1024*1024
        with open(outfile, "wb") as f:
            for chunk in resp.iter_content(chunk_size=bytes_in_mb):
                if chunk:
                    f.write(chunk)
        if os.path.exists(outfile):
            ns = time.time() - start
            mb = os.path.getsize(outfile)/float(bytes_in_mb)
            logger.info('%s (%3.2f (MB) %3.2f (MB/s))',
                        outfile, mb, mb/ns)
        logger.info("Download of %s complete.", outfile)
    except Exception as exc:
        logger.error("Could not download %s, Response: %s", url, exc)
