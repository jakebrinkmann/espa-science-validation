"""Entry point to the retrieve_data.espa_orders_api.py script"""

import argparse

from retrieve_data.espa import espa_orders_api


def main():
    parser = argparse.ArgumentParser(description=espa_orders_api.__doc__)

    required_named = parser.add_argument_group("Required named arguments")

    required_named.add_argument("-i", dest="txt_in", type=str, required=True, action="store",
                                help="Full path and name of the .txt file containing the ESPA orders")

    required_named.add_argument("-o", dest="outdir", type=str, required=True, action="store",
                                help="Full path to the output directory.  Ideally corresponds to the specified "
                                     "ESPA environment.")

    required_named.add_argument("-u", dest="username", type=str, required=True, action="store",
                                help="ESPA user name")

    required_named.add_argument("-env", dest="espa_env", type=str, choices=["ops", "tst", "dev"], required=True,
                                help="ESPA environment")

    args = parser.parse_args()

    espa_orders_api.get_orders(**vars(args))

    return None


if __name__ == "__main__":
    main()
