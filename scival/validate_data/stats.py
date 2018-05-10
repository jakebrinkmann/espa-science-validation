"""Purpose: get comparision results, run statistics, write out to files."""

import os
import csv
import numpy as np
import logging


def pct_diff_raster(ds_tband: np.ndarray, ds_mband: np.ndarray, diff_rast: np.ndarray, nodata: int=-9999) -> np.ndarray:
    """
    Calculate percent difference raster
    :param ds_tband: array of test raster
    :param ds_mband: array of master raster
    :param diff_rast: array of difference raster
    :param nodata: int representing no data value
    :return:
    """
    # get min and max of both rasters' worth of data
    mins = []
    maxs = []  # empty variable to compare both rasters' mins
    ds_tband = np.ma.masked_where(ds_tband == nodata, ds_tband)
    ds_mband = np.ma.masked_where(ds_mband == nodata, ds_mband)

    mins.append(np.min(ds_tband))
    mins.append(np.min(ds_mband))
    rmin = np.min(mins)

    maxs.append(np.max(ds_tband))
    maxs.append(np.max(ds_mband))
    rmax = np.max(maxs)

    # make a pct diff raster
    pct_diff_raster = ((np.abs(diff_rast) / np.abs(float(rmax - rmin))) * 100)

    logging.warning("Percent difference raster created.")

    return pct_diff_raster


def img_stats(test: str, mast: str, diff_img: np.ndarray, dir_in: str, fn_in: str, dir_out: str, sds_ct: int=0) -> None:
    """
    Log stats from array
    :param test: name of test file
    :param mast: name of master file
    :param diff_img: image array
    :param dir_in: directory where test data exists
    :param fn_in: input filename (to identify csv entry)
    :param dir_out: output directory
    :param sds_ct: index of SDS (default=0)
    :return:
    """
    diff_img = np.ma.masked_where(diff_img == 0, diff_img)

    fn_out = dir_out + os.sep + "stats.csv"
    logging.info("Writing stats for {0} to {1}.".format(fn_in, fn_out))

    file_exists = os.path.isfile(fn_out)

    # Changed "ab" to "a", using python 3.6 was getting TypeError: a bytes-like object is required, not 'str'
    with open(fn_out, "a") as f:
        writer = csv.writer(f)

        # write header if file didn't already exist
        if not file_exists:
            writer.writerow(("dir",
                             "test_file",
                             "master_file",
                             "mean",
                             "min",
                             "max",
                             "25_percentile",
                             "75_percentile",
                             "1_percentile",
                             "99_percentile",
                             "std_dev",
                             "median"))

        writer.writerow((dir_in,
                        test + "_" + str(sds_ct),
                        mast + "_" + str(sds_ct),
                        np.mean(diff_img),
                        np.amin(diff_img),
                        np.amax(diff_img),
                        np.percentile(diff_img.compressed(), 25),
                        np.percentile(diff_img.compressed(), 75),
                        np.percentile(diff_img.compressed(), 1),
                        np.percentile(diff_img.compressed(), 99),
                        np.std(diff_img),
                        np.median(diff_img.compressed())))

        return None
