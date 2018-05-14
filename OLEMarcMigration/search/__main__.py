from argparse import ArgumentParser
from marcextraction.lookup import MarcFieldLookup
from marcextraction.interfaces import SolrIndexSearcher
from marcextraction.utils import find_ole_bib_numbers
from sys import stdout, stderr

def show_lookups(args):
    output = MarcFieldLookup.show_valid_lookups(pretty_print=True)
    stdout.write(output)

def search_func(args):
    searcher = SolrIndexSearcher(args.index_url, 'ole')
    results = searcher.search(args.query_term, args.field_lookup, args.subfield_lookup)
    output = []
    for n in results:
        output += n.get("controlfield_001")
    print(output)

def main():
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
            print("hi")
            search_func(args)
        return 0
    except KeyboardInterrupt:
        return 131