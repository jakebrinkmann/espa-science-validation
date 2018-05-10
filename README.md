# espa-science-validation
Compare the outputs from different ESPA environments

### Support Information
This project is unsupported software provided by the U.S. Geological Survey (USGS) Earth Resources Observation and Science (EROS) Land Satellite Data Systems (LSDS) Project.  For questions regarding products produced by this source code, please contact us at custserv@usgs.gov.

### Disclaimer
This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.

### Requirements

* python >= 3.5
    * numpy
    * matplotlib
    * lxml
    * requests
    * scikit_image
* gdal >= 1.11

### Installation

* Recommended to use conda: `conda create -n scival python=3 GDAL; activate scival`
* Install python dependencies: `pip install -e .`

### Running

These tools allow for the independent validation of higher level science products generated from Level-1 Landsat
data that are served via the EROS Science Processing Architecture (ESPA).

As algorithms are continually developed, it is necessary to perform these validations prior to public release.  This
allows for the identification of unwanted artifacts and the confirmation of desired changes.
The ordering interface via an API is also tested to ensure consistent and expected performance for public use.

A pre-designed order is provided in order_specs.py.  Additional orders can be added to the dict, and their
corresponding keyword can be passed to espa_order.  If no keyword is given, then the original full test order will be
issued.

Example usage and logical order:

1) `espa_order -u <USERNAME> -env <ESPA_ENVIRONMENT> -o <OUTPUT_DIRECTORY> --order original`

2) `espa_download -u <USERNAME> -env <ESPA_ENVIRONMENT> -o <ESPA_ENVIRONMENT>/ -i order_123456789.txt`

3) `espa_qa -m MASTER/ -t TEST/ -o RESULTS/ --verbose --include-nodata`
