import logging
logger = logging.getLogger('scival')
logger.handlers = []

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
