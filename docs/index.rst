.. convert_marc_to_iiif_webapp documentation master file, created by
   sphinx-quickstart on Wed Jan 10 15:24:36 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Documentation for findMarcRecordsInOLE 
=================================================

This is a command-line tool intended to enable developers at UChicago library to search for MARC records
in OLE and get back the up-to-date full records matching their query.

After installation, you can run the CLI application by typing

.. code-block: bash
    find_records -h
    usage: find_records [-h] [--version] {show_lookups,searching} ...
    positional arguments:
        {show_lookups,searching}    how to retrieve valid lookup labels
    optional arguments:
        -h, --help            show this help message and exit
        --version             show program's version number and exit

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   autodoc



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
