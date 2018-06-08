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
* GDAL >= 1.11

### Installation

* Recommended to using conda: `conda create -n scival python=3 GDAL; source activate scival`
* Install python dependencies: `pip install -e .`


### Configuration

Some arguments can be configured from the environment:

arg | summary
-|-
`ESPA_SCIVAL_ESPA_USERNAME` | A valid [ERS][1] account
`ESPA_SCIVAL_ESPA_ENV` | Select a different ESPA host


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

1) `scival espa order -u <USERNAME> -e <ESPA_ENVIRONMENT> -o <OUTPUT_DIRECTORY> --order original.test1`

1) `scival espa download -u <USERNAME> -e <ESPA_ENVIRONMENT> -o <OUTPUT_DIRECTORY>/ -i order_123456789.txt`

1) `scival -vv qa compare -m MASTER/ -t TEST/ -o RESULTS/ --archive --include-nodata`

Instead of ESPA, some data can be retrieved immedately from EarthExplorer
(with Machine-to-Machine download):

1) `scival ee download -u <USERNAME> -e <EE_ENVIRONMENT> -o <OUTPUT_DIRECTORY>/ --search ard_1`


[1]: https://ers.cr.usgs.gov/
