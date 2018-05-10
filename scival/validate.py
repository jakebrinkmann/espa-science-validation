"""An entry point for the qa module"""

import argparse

from validate_data.qa import qa_data


def main():
    parser = argparse.ArgumentParser()

    required_named = parser.add_argument_group("Required named arguments")

    required_named.add_argument("-m", dest="dir_mast", type=str, required=True, action="store",
                                help="The full path to the Master directory")

    required_named.add_argument("-t", dest="dir_test", type=str, required=True, action="store",
                                help="The full path to the Test directory")

    required_named.add_argument("-o", dest="dir_out", type=str, required=True, action="store",
                                help="The full path to the Results directory")

    parser.add_argument("-x", dest="xml_schema", type=str, required=False, action="store",
                        help="Full path to XML schema")

    parser.add_argument("--no-archive", dest="archive", required=False, action="store_false",
                        help="Look for individual files insead of g-zipped archives")

    parser.add_argument("--verbose", dest="verbose", required=False, action="store_true",
                        help="Enable verbose logging")

    parser.add_argument("--include-nodata", dest="incl_nd", required=False, action="store_true",
                        help="Do not mask NoData values")

    args = parser.parse_args()

    qa_data(**vars(args))

    return None


if __name__ == "__main__":
    main()
