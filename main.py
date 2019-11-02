#!/usr/bin/env python3
"""Wikipedia first link parser """

import logging
import argparse
import pprint
from wikigraph.parser import WikiParser
from wikigraph.analysis import WikiAnalysis

def main():
    # Parse Arguments
    parser = argparse.ArgumentParser(description='What does this program do?')
    parser.add_argument('-l', '--log', dest='loglevel', default='ERROR',
            help='log level to output (default: ERROR)')
    parser.add_argument('--log-file', dest='logfile',
            help='destination file to write logging output')
    parser.add_argument('-e', '--ends', dest='ends', action='store_true', default=False,
            help='Print report of end pages/cycles instead of per page')
    parser.add_argument('filename', help='The wikipedia bz2 filename')
    args = parser.parse_args()

    try:
        loglevel = getattr(logging, args.loglevel.upper())
    except:
        parser.error("Invalid LOGLEVEL")

    # Configure loggin
    logging.basicConfig(level=loglevel, 
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
            filename=args.logfile)
    logger = logging.getLogger(__name__)

    logger.info("Starting")
    wp = WikiParser(args.filename)
    wp.parse()
    logger.info("Parsed")

    #wp.walk("Salt")

    wa = WikiAnalysis(wp.links)
    visitors = wa.all_visitors()
    ends = wa.all_ends()
    logger.info("Analyzed")

    if args.ends:
        logger.info("Printing 'ends' report")
        for record in ends:
            print(record)
    else:
        logger.info("Printing 'per page' report")
        for record in visitors:
            print(*record)


    logger.info("Done")

if __name__ == '__main__':
    main()

