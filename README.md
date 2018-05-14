# convert_marc_to_iiif_webapp [![v0.0.1](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/uchicago-library/convert_marc_to_iiif_webapp/releases)

[![Build Status](https://travis-ci.org/uchicago-library/convert_marc_to_iiif_webapp.svg?branch=master)](https://travis-ci.org/uchicago-library/convert_marc_to_iiif_webapp) [![Coverage Status](https://coveralls.io/repos/github/uchicago-library/convert_marc_to_iiif_webapp/badge.svg?branch=master)](https://coveralls.io/github/uchicago-library/convert_marc_to_iiif_webapp?branch=master) [![Documentation Status](https://readthedocs.org/projects/convert_marc_to_iiif_webapp/badge/?version=latest)](http://convert_marc_to_iiif_webapp.readthedocs.io/en/latest/?badge=latest)

A web application intended to be able to a) extract a MARC record from the Solr index and b) generate IIIF record

## Prerequisites

1. python3.6
1. virtualenv
1. [marc2iiif](https://github.com/uchicago-library/marc2iiif)
1. [marcExtraction](https://github.com/uchicago-library/extract_marc_from_vufind)
1. [pyiiif](https://github.com/uchicago-library/pyiiif)

## How to create a virtual environment on Linux or Mac OS

1. mkdir [new directory for your project]
1. cd [new directory for your project]
1. python3 -m venv venv 

## How to create a virtual environment on Windows

1. pip install virtualenvwrapper-win
1. mkvirtualenv [name of new environment]

## How to activate a virtual environment in Linux or Mac OS

1. source [path to virtual environment]/bin/activate

## How to activate a virtual environment in Windows

1. [path to virtual environment]/Scripts/activate

## How to install a library

1. make sure the virtualenv you want to install the library is active!
1. git clone https://github.com/user/[repo].git
1. cd [repo]
1. pip install -r requirements.txt
1. python setup.py install

Quickstart

1. git clone git@github.com:uchicago-library/extract_marc_from_vufind.git
1. cd extract_marc_from_vufind
1. install all requirements for pre-requisities libraries and the libraries
1. pip install -r requirements.txt
1. python setup.py install

## Documentation

[Usage Documentation](https://github.com/uchicago-library/findMarcRecordsInOLE/wiki)

# Author
Tyler Danstrom <tdanstrom@uchicago.edu>
