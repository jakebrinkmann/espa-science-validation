""" Utilities for host system interaction """

import os
import time
import sys
import logging
import datetime

import requests

from . import logger


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

    outdir = os.path.basename(outfile)
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    t = time.time()
    resp = requests.get(url, stream=True)

    if resp.ok:
        with open(outfile, "wb") as f:
            for chunk in resp.iter_content(chunk_size=2048):
                f.write(chunk)
        if os.path.exists(outfile):
            logger.info('MB/s: %d (%s)',
                        os.path.getsize(outfile) / 1024 /
                        (time.time() - t) / 1024,
                        outfile)
        logger.info("Download of %s complete.", url)
    else:
        logger.error("Could not download %s, Response: %s", url, resp)
