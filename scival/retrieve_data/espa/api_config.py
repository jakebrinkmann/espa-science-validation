"""Some useful data structures and functions"""

import datetime

espa_env = {
    "dev": "https://espa-dev.cr.usgs.gov",
    "tst": "https://espa-tst.cr.usgs.gov",
    "ops": "https://espa.cr.usgs.gov"
}

api_urls = {
    "status": "/api/v1/item-status/",
    "order": "/api/v1/order/"
}


def timestamp() -> str:
    """
    Get system timestamp for output text file name in the format YYYYMMDDhhmmss
    :return:
    """
    return str(int(float(str(datetime.datetime.now()).replace('-', '')
                         .replace(':', '').replace(' ', ''))))
