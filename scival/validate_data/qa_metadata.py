"""qa_metadata.py"""

import os

from lxml import etree

from scival.validate_data.file_io import Cleanup, ImWrite
from scival.validate_data.qa_images import ArrayImage
from scival import logger


class MetadataQA:
    @staticmethod
    def check_xml_schema(test, schema):
        """Ensure XML matches ESPA schema.
        :param test: <str> XML metadata file to compare with schema.
        :param schema: <str> Path to XML schema file.
        :return: None
        """
        # read schema
        xmlschema = etree.XMLSchema(etree.parse(schema))

        # read XML
        xmlfile = etree.parse(test)

        # do validation
        result = xmlschema.validate(xmlfile)

        if result:
            logger.warning('XML file {0} is valid with XML schema {1}.'
                            .format(test, schema))

        else:
            logger.critical('XML file {0} is NOT valid with XML schema {1}.'
                             .format(test, schema))

    @staticmethod
    def check_text_files(test, mast, ext):
        """Check master and test text-based files (headers, XML, etc.)
        line-by-line for differences.
        Sort all the lines to attempt to capture new entries.

        Args:
            test <str>: path to test text file
            mast <str>: path to master text file
            ext <str>: file extension (should be .txt, .xml or .gtf
        """
        logger.info("Checking {0} files...".format(ext))

        test, mast = Cleanup.remove_nonmatching_files(test, mast)

        # Do some checks to make sure files are worth testing
        if mast is None or test is None:
            logger.warning("No {0} files to check in test and/or mast "
                            "directories.".format(ext))
            return

        if len(mast) != len(test):
            logger.error("{0} file lengths differ. Master: {1} | Test:"
                          " {2}".format(ext, len(mast), len(test)))
            return

        for i, j in zip(test, mast):
            topen = open(i)
            mopen = open(j)

            # Read text line-by-line from file
            file_topen = topen.readlines()
            file_mopen = mopen.readlines()

            # Close files
            topen.close()
            mopen.close()

            # Check file names for name differences.
            # Print non-matching names in details.
            # get file names
            i_fn = i.split(os.sep)[-1]
            j_fn = j.split(os.sep)[-1]
            if i_fn != j_fn:
                logger.error("{0} file names differ. Master: {1} | Test: {2}".
                              format(ext, j, i))
                return
            else:
                logger.info("{0} file names equivalent. Master: {1} | Test: "
                             "{2}".format(ext, j, i))

            # Check open files line-by-line (sorted) for changes.
            # Print non-matching lines in details.
            txt_diffs = set(file_topen).difference(set(file_mopen))
            if len(txt_diffs) > 0:
                for k in txt_diffs:
                    logger.error("{0} changes: {1}".format(ext, k))

            else:
                logger.info("No differences between {0} and {1}.".
                             format(i, j))

    @staticmethod
    def check_jpeg_files(test: list, mast: list, dir_out: str) -> None:
        """
        Check JPEG files (i.e., Gverify or preview images) for diffs in file size or file contents.  Plot difference
        image if applicable
        :param test: List of paths to test jpg files
        :param mast: List of paths to master jpg files
        :param dir_out: Full path to output directory
        :return:
        """
        test, mast = Cleanup.remove_nonmatching_files(test, mast)
        logger.info("Checking JPEG preview/gverify files...")

        if mast is None or test is None:
            logger.error("No JPEG files to check in test and/or mast "
                          "directories.")

        else:
            for i, j in zip(test, mast):

                # Compare file sizes
                if os.path.getsize(i) != os.path.getsize(j):
                    logger.warning("JPEG file sizes do not match for "
                                    "Master {0} and Test {1}...\n".
                                    format(j, i))
                    logger.warning("{0} size: {1}".format(
                        i, os.path.getsize(i)))
                    logger.warning("{0} size: {1}".format(
                        j, os.path.getsize(j)))

                else:
                    logger.info("JPEG files {0} and {1} are the same "
                                 "size".format(j, i))

                # diff images
                result = ArrayImage.check_images(i, j)

                if result:
                    ImWrite.plot_diff_image(test=i, mast=j, diff_raster=result, fn_out=i.split(os.sep)[-1],
                                            fn_type="diff_", dir_out=dir_out)
