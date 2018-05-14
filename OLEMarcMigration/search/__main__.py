"""a console-script to  allow a library dev to search for records in OLE by arbitrary MARC fields
"""

__author__ = "Tyler Danstrom"
__email__ = "tdanstrom@uchicago.edu"
__version__ = "0.0.1"

from argparse import ArgumentParser
from marcextraction.lookup import MarcFieldLookup
from marcextraction.interfaces import SolrIndexSearcher
from marcextraction.utils import find_ole_bib_numbers
from sys import stdout, stderr

def show_lookups(args):
    """a function to get the valid lookup labels and printing it to the screen

    The developer should use the MARC field labels in the field_lookup parameter of the searching subparser
    and the appropriate SubField label in the subfield_lookup paramter of the same subparser

    Returns:
        stdout. A pretty-printed string sent to stdout for display in a console.
    """
    output = MarcFieldLookup.show_valid_lookups(pretty_print=True)
    stdout.write(output)

def search_func(args):
    """a function to search the requested Solr index for the query term matching the desired MARC field

    Returns:
        list. A list of XML extracted from the Solr index or an empty list if no items matched the query.
    """
    searcher = SolrIndexSearcher(args.index_url, 'ole')
    results = searcher.search(args.query_term, args.field_lookup, args.subfield_lookup)
    for n in results:
        stdout.write("{}\n".format(n.get("controlfield_001")))

def main():
    """the main function of the console-script.

    There are two sub-parsers: show and searching

    - show takes no parameters and simply returns a pretty-printed display of the MARC field and subfield
      labels necessary to do a field-targetted search
    - searching takes three parameters and returns to stdout the bib numbers of the matching records.
        - query_term is the string that you want to find in the requested MARC field/subfield. Searches include stemming.
        - index_url is the url of the Solr index to run the search against
        - field_lookup is the MARC field label from show that the developer wants to target
        - subfield_lookup is the subfield label from the show that the developer wants to do a target search in
    """
    try:
        parser = ArgumentParser()
        subparsers = parser.add_subparsers(help='how to retrieve valid lookup labels', dest='which')
        show = subparsers.add_parser('show_lookups')
        search = subparsers.add_parser('searching')
        show.set_defaults(which='show')
        search.set_defaults(which='searching')
        search.add_argument("query_term", help="A string that you want to search the OLE index stemmed for matching results", 
                            action='store', type=str)
        search.add_argument("index_url", help="A url to the OLE index you want to search", action='store', type=str)
        search.add_argument("field_lookup", help="")
        search.add_argument("subfield_lookup", help="")
        parser.add_argument("--version", action='version', version='%(prog)s 1.0')
        args = parser.parse_args()
        if args.which == 'show':
            show_lookups(args)
        elif args.which == 'searching':
            search_func(args)
        return 0
    except KeyboardInterrupt:
        return 131