""" Utilities for host system interaction """

import sys
import logging
import datetime


logger = None

def setup_logger(verbosity, stream='stderr'):
    """ configure logging via verbosity level of between 0 and 2 corresponding
    to log levels warning, info and debug respectfully. """
    global logger

    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    log_out = "log_{0:%Y%m%d-%H%M%S}.log".format(datetime.datetime.now())
    fh = logging.FileHandler(log_out)
    fh.setFormatter(log_formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    log_level = max(logging.DEBUG, logging.WARNING - logging.DEBUG*verbosity)
    ch = logging.StreamHandler(stream=getattr(sys, stream.lower()))
    ch.setFormatter(log_formatter)
    fh.setLevel(log_level)
    logger.addHandler(ch)
