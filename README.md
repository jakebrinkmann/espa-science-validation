# espa-science-validation
Various tools for performing QA on and validating ESPA products

### Support Information
This project is unsupported software provided by the U.S. Geological Survey (USGS) Earth Resources Observation and Science (EROS) Land Satellite Data Systems (LSDS) Project.  For questions regarding products produced by this source code, please contact us at custserv@usgs.gov.

### Disclaimer
This software is preliminary or provisional and is subject to revision. It is being provided to meet the need for timely best science. The software has not received final approval by the U.S. Geological Survey (USGS). No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the functionality of the software and related material nor shall the fact of release constitute any such warranty. The software is provided on the condition that neither the USGS nor the U.S. Government shall be held liable for any damages resulting from the authorized or unauthorized use of the software.

### Requirements

python >= 3.5

gdal

numpy

matplotlib

pandas

pyyaml

lxml

requests

scikit_image

### Installation

``$python setup.py install``

### Running

````$espa_order  -u <user-name> -env <env> -o <out-directory> ````

````$espa_download -u <user-name> -env <env> -o <out-directory> -i <txt-in>````

``$espa_qa -m <master-directory> -t <test-directory> -o <results-directory>``

