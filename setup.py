from setuptools import setup, find_packages


def version():
    return open('version.txt').read()


def readme():
    return open('README.md').read()


setup(name='espa-science-validation',
      version=version(),
      description='Compare the outputs from different ESPA environments',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='usgs eros lsrd espa',
      url='https://github.com/USGS-EROS/espa-science-validation',
      author='USGS EROS LSRD https://eros.usgs.gov/',
      author_email='custserv@usgs.gov',
      license='Unlicense',
      packages=find_packages(),
      python_requires=">=3.5",
      install_requires=[
          "matplotlib",
          "numpy",
          "gdal",
          "requests",
          "lxml",
          "scikit_image"
      ],
      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[test]
      extras_require={
          'test': [
              'pytest',
              'pytest-cov',
              'vcrpy',
              'hypothesis',
                  ],
          'doc': [
              'sphinx',
              'sphinx-autobuild',
              'sphinx_rtd_theme'],
          'dev': [
              'pylint',
              'mypy',
              'pycodestyle',
              'pydocstyle',
          ],
      },
      entry_points={"console_scripts": [
          "espa_download = scival.download:main",
          "espa_order = scival.place_order:main",
          "espa_qa = scival.validate:main"
      ]},
      include_package_data=True,
      zip_safe=False
)
