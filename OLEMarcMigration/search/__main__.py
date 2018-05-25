"""a console-script to  allow a library dev to search for records in OLE by arbitrary MARC fields
"""

__author__ = "Tyler Danstrom"
__email__ = "tdanstrom@uchicago.edu"
__version__ = "2.0.0"

from argparse import ArgumentParser, Action, ArgumentError
from marcextraction.interfaces import SolrIndexSearcher, OLERecordFinder
from marcextraction.utils import find_ole_bib_numbers
from marclookup.lookup import MarcField, MarcFieldBrowse
from os import environ, getcwd
from os.path import exists, join
from sys import stdout, stderr
from urllib.parse import urlparse
from uuid import uuid4
from xml.etree import ElementTree

# run using the following command 
# OLE_INDEX=[uchicago ole sru api] SOLR_INDEX=[uchicago ole solr index] find_records -h

OLE_INDEX = environ["OLE_INDEX"]
SOLR_INDEX = environ["SOLR_INDEX"]

class CombineWithProperFieldLookup(Action):
    """a custom action class for argparse to raise ArgumentError if field_lookup and field_label_lookup used with wrong subfield lookup
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(CombineWithProperFieldLookup, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, args, values, options_string=None):
        if (args.field_lookup != None) and (self.dest == 'subfield_label_lookup'):
            raise ArgumentError(self, "Cannot be combined with -f/--field_lookup")
        elif args.field_label_lookup != None and (self.dest == 'subfield_lookup'):
            raise ArgumentError(self, "Cannot be combined with -fl/--field_label_lookup")
        else:
            setattr(args, self.dest, values)

def show_lookups(args):
    """a function to get the valid lookup labels and printing it to the screen

    The developer should use the MARC field labels in the field_lookup parameter of the searching subparser
    and the appropriate SubField label in the subfield_lookup paramter of the same subparser

    Args:
        args (ParseResult)

    Returns:
        stdout. A pretty-printed string sent to stdout for display in a console.
    """

    output = MarcFieldBrowse()
    stdout.write(str(output))

def search_func(args):
    """a function to search the requested Solr index for the query term matching the desired MARC field

    Args:
        args (ParseResult)

    Returns:
        list. A list of XML extracted from the Solr index or an empty list if no items matched the query.
    """
    ole_url = urlparse(OLE_INDEX)
    searcher = SolrIndexSearcher(SOLR_INDEX, 'ole')
    the_field = MarcField(field=args.field)
    subfields = [x.code for x in the_field.subfields if x.code in args.subfields]
    marc_number = the_field.field
    results = searcher.search(args.query_term, marc_number, args.subfields, rows=args.number_of_records)
    records = []
    if args.extract_records:
        for result in results:
            record = OLERecordFinder(result, ole_url.netloc, ole_url.scheme, ole_url.path)
            check, records = record.get_record()
            if check:
                for record in records:
                    xml_doc = ElementTree.ElementTree(ElementTree.fromstring(record.decode("utf-8")))
                    new_filename = join(getcwd(), uuid4().hex+".xml")
                    xml_doc.write(new_filename, xml_declaration=True)
                    stdout.write("wrote new record to {}\n".format(new_filename))
    else:
        count = 0
        for result in  results:
            stdout.write("found record with bib number {}\n".format(result))
            count += 1
        stdout.write("total records: {}\n".format(count))

def main():
    """the main function of the console-script.

    There are two sub-parsers: show and searching

    - show takes no parameters and simply returns a pretty-printed display of the MARC field and subfield
      labels necessary to do a field-targetted search
    - searching takes up to three parameters and returns to stdout the bib numbers of the matching records or saves the records 
      to your current working directory
    """
    try:
        parser = ArgumentParser()
        subparsers = parser.add_subparsers(help='how to retrieve valid lookup labels', dest='which')
        show = subparsers.add_parser('show_lookups')
        search = subparsers.add_parser('searching')
        show.set_defaults(which='show')
        search.set_defaults(which='searching')
        search.add_argument("-f", "--field", help="The field number for the MARC21 field that you want to search in. Defaults to 245", action='store', type=str, default='245')
        search.add_argument("-sf", "--subfields", help="The labels for the subfields that you want to search in. Defaults to ['a']", nargs="+", type=str, default=['a'])
        search.add_argument("-q", "--query_term", help="A string that you want to search the OLE index stemmed for matching results Default is wildcard.",
                             action='store', type=str, default='*')
        search.add_argument("--extract_records", action='store_true', default=False, help="Use this flag if you don't actually want to save the records to disk yet")
        search.add_argument("-n", "--number_of_records", help="Enter the total number of records that you want to extract. Default is 10.", action='store', type=int, default=10)
        parser.add_argument("--version", action='version', version='%(prog)s 1.0')
        args = parser.parse_args()
        if args.which == 'show':
            show_lookups(args)
        elif args.which == 'searching':
            search_func(args)
        return 0
    except KeyboardInterrupt:
        return 131
