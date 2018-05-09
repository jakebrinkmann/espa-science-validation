"""These tools allow for the independent validation of higher level science products generated from Level-1 Landsat
data that are served via the EROS Science Processing Architecture (ESPA).

As algorithms are continually developed, it is necessary to perform these validations prior to public release.  This
allows for the identification of unwanted artifacts and the confirmation of desired changes.
The ordering interface via an API is also tested to ensure consistent and expected performance for public use.

A pre-designed order is provided in order_specs.py.  Additional orders can be added to the dict, and their
corresponding keyword can be passed to espa_order.  If no keyword is given, then the original full test order will be
issued.

Example usage and logical order:

1) espa_order -u USERNAME -env ESPA_ENVIRONMENT -o OUTPUT_DIRECTORY/ --order original

2) espa_download -u USERNAME -env ESPA_ENVIRONMENT -o ESPA_ENVIRONMENT/ -i order_123456789.txt

3) espa_qa -m MASTER/ -t TEST/ -o RESULTS/ --verbose --include-nodata

"""

from setuptools import setup, find_packages

setup(
    name="espa_validation",

    version="0.1.0",

    packages=find_packages(),

    install_requires=[
        "matplotlib",
        "numpy",
        "gdal",
        "requests",
        "pandas",
        "lxml",
        "scikit_image",
        "pyyaml"
    ],

    entry_points={"console_scripts": [
        "espa_download = espa_validation.download:main",
        "espa_order = espa_validation.place_order:main",
        "espa_qa = espa_validation.validate:main"
    ]},

    dependency_links=["https://github.com/conda-forge/"],

    python_requires=">=3.5",

    author="USGS EROS LSRD https://eros.usgs.gov/",

    author_email="custserv@usgs.gov",

    long_description=__doc__,

    description="A series of validation tools that can be used to compare the outputs "
                "from different ESPA environments.",

    license="Public Domain",

    url="https://github.com/USGS-EROS/espa-science-validation"
)
