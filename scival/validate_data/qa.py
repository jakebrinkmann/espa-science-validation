"""
qa.py

Purpose: Perform QA on georeferenced images and associated metadata. Designed
         originally to support the Earth Resources Observation and Science
         (EROS) Science Processing Architecture
         (ESPA; https://espa.cr.usgs.gov/.)
         Extract and clean up data automatically (if necessary.)
         Report results in logfile, CSV and plots.

Author:   Steve Foga
Contact:  steven.foga.ctr@usgs.gov
Created:  21 December 2016
Modified: 21 March 2017

Changelog:
    21 Dec 2016: Original development.
    12 Jan 2017: Fixed errors, formatting.
    02 Feb 2017: Added switch for archived or non-archived inputs; modified
                 stats output on plots; fixed nodata filtering for histograms;
                 wrote XML parsing code (but not usage of said output); fixed
                 file removal logic in file_io.py
    09 Mar 2017: Fixed error handling for files that have mis-matched SDS
                 Updated TODOs
    15 Mar 2017: Added optional XML schema validation; fixed typos
    21 Mar 2017: Added flag to include/exclude nodata from calculations

Modified February and March 2018
Daniel Zelenak
daniel.zelenak.ctr@usgs.gov

    Changelog:
        Add PEP 484 typing, trying to make it more clear what types are being passed
        Change qa_data __doc__ to reStructuredText format
        Addressed JPEG testing exceptions resulting from passing strings instead of lists
        In qa_metadata.MetadataQA.check_jpeg_files added ImWrite.plot_diff_image and passing all expected params
"""

import sys
import os
import logging
import time

from scival.validate_data.file_io import Extract, Find, Cleanup
from scival.validate_data.qa_images import GeoImage
from scival.validate_data.qa_metadata import MetadataQA


# TODO (med): Enable SDS sorting with NetCDF, HDF files.
# TODO (low): Implement checking file names with XML.

# TODO (low): Only CleanUp files that pass all matching tests, leave files with differences to allow further testing.

def qa_data(dir_mast: str, dir_test: str, dir_out: str, archive: bool = True, xml_schema: str = None,
            incl_nd: bool = False) -> None:
    """
    Function to check files and call appropriate QA module(s)
    :param dir_mast: Full path to the master directory
    :param dir_test: Full path to the test directory
    :param dir_out: Full path to the QA output directory
    :param archive: If True, will clean up existing files and extract from archives
    :param xml_schema: Full path to XML files, default is None
    :param incl_nd: If True, include NoData in comparisons
    :return:
    """
    # start timing code
    t0 = time.time()

    # create output dir if it doesn't exist
    if not os.path.exists(dir_out):
        os.makedirs(dir_out)

    if archive:
        # do initial cleanup of input directories
        Cleanup.cleanup_files(dir_mast)

        Cleanup.cleanup_files(dir_test)

        # create output directory if it doesn't exist
        if not os.path.exists(dir_out):
            os.makedirs(dir_out)

        # read in .tar.gz files
        test_files = Find.find_files(dir_test, ".gz")

        mast_files = Find.find_files(dir_mast, ".gz")

        # Extract files from archive
        Extract.unzip_gz_files(test_files, mast_files)

    # find only the deepest dirs
    test_dirs = sorted([r for r, d, f in os.walk(dir_test) if not d])

    mast_dirs = sorted([r for r, d, f in os.walk(dir_mast) if not d])

    if len(test_dirs) != len(mast_dirs):
        logging.critical("Directory structure of Master differs from Test.")

        sys.exit(1)

    for i in range(0, len(test_dirs)):
        # Find extracted files
        all_test = sorted(Find.find_files(test_dirs[i], ".*"))

        all_mast = sorted(Find.find_files(mast_dirs[i], ".*"))

        # Find unique file extensions
        exts = Find.get_ext(all_test, all_mast)

        for ext in exts:
            logging.info("Finding {0} files...".format(ext))

            test_f = Find.find_files(test_dirs[i], ext)

            mast_f = Find.find_files(mast_dirs[i], ext)

            logging.info("Performing QA on {0} files located in {1}".format(ext, dir_test))

            logging.info("Test files: {0}".format(test_f))

            logging.info("Mast files: {0}".format(mast_f))

            # remove any _hdf.img files found with .img files
            if ext == ".img":
                test_f = Cleanup.rm_files(test_f, "_hdf.img")

                mast_f = Cleanup.rm_files(mast_f, "_hdf.img")

            # if a text-based file
            if (ext.lower() == ".txt" or ext.lower() == ".xml"
                    or ext.lower() == ".gtf" or ext.lower() == ".hdr"
                    or ext.lower() == ".stats"):

                MetadataQA.check_text_files(test_f, mast_f, ext)

                # if text-based file is xml
                if ext.lower() == ".xml" and xml_schema:
                    MetadataQA.check_xml_schema(test_f, xml_schema)

                    MetadataQA.check_xml_schema(mast_f, xml_schema)

            # if non-geo image
            elif ext.lower() == ".jpg":
                MetadataQA.check_jpeg_files(test_f, mast_f, dir_out)

            # if no extension
            elif len(ext) == 0:
                continue

            # else, it's probably a geo-based image
            else:
                GeoImage.check_images(test_f, mast_f, dir_out, ext,
                                      include_nd=incl_nd)

    if archive:
        # Clean up files
        Cleanup.cleanup_files(dir_mast)

        Cleanup.cleanup_files(dir_test)

    # end timing
    t1 = time.time()

    m, s = divmod(t1 - t0, 60)

    h, m = divmod(m, 60)

    logging.warning("Total runtime: {0}h, {1}m, {2}s.".format(h, round(m, 3), round(s, 3)))

    print("Done.")

    return None
