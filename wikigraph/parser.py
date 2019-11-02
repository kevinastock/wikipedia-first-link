"""Parse a wiki dump into a dict representing first links"""

import bz2
import xml.parsers.expat as expat
import re
import string

import logging
logger = logging.getLogger(__name__)

""" Regex for finding links within peel """
link_re = re.compile("(?P<link>[^[\]:|]*)(\|[^\]][^\]]*)?\]\]")

class LinkSearch:
    def __init__(self, src, debug_info=None):
        self.tokens = { '{{':'}}', '[[':']]', '(':')' , "''":"''"}
        self.debug_info = debug_info
        self.src = src
        self.token = None
        self.count = 0
        self.opened = False

    def peel(self):
        """ Remove leading portion of self.src upto a opening token or close 
        of currently opened token"""
        if self.count == 0:
            best_off, best_tok = len(self.src), None
            for token in self.tokens:
                d = self.src.find(token, 0, best_off)
                if d == -1:
                    d = len(self.src)
                if d < best_off:
                    best_off, best_tok = d, token
            if not best_tok:
                self.src = ''
                return
            self.token = best_tok
            self.src = self.src[best_off + len(best_tok):]
            self.count = 1
            self.opened = True
        else:
            close_pos = self.src.find(self.tokens[self.token])
            if close_pos < 0:
                logger.debug("Couldn't close " + self.token + ' [' + repr(self.debug_info) + ']')
                self.token = None
                self.count = 0
                return
            open_pos = self.src.find(self.token, 0, close_pos)
            if open_pos >= 0 and open_pos < close_pos:
                self.count += 1
                self.src = self.src[open_pos + len(self.token):]
                self.opened = True
            else:
                self.count -= 1
                self.src = self.src[close_pos + len(self.token):]
                self.opened = False

    def first_link(self):
        """ Find the first link on a page """
        logger.debug(self.src)
        while self.src:
            self.peel()
            logger.debug(self.src)
            if self.token == '[[' and self.count == 1 and self.opened:
                m = link_re.match(self.src)
                if m:
                    return self.clean_link(m.group('link'))
        return None

    def clean_link(self, link):
        """ Canonicalize name of wikipedia standards """
        link = link.replace('_', ' ')
        if '#' in link:
            link = link[0:link.find('#')]
        if link and link[0] in string.ascii_lowercase:
            return link[0].upper() + link[1:]
        return link

class WikiParser:
    def __init__(self, filename, special=False):
        self.xml = bz2.BZ2File(filename)
        self.last_tag = None
        self.title = None
        self.first_link = None
        self.is_redirect = False
        self.links = {}
        self.redirects = {}

        def start_element(name, attrs):
            self.last_tag = name
            if name == 'redirect':
                self.is_redirect = True

        def char_data(data):
            if self.last_tag == 'title':
                self.title = data
                logger.debug("Title: " + data)
            elif self.last_tag == 'text':
                self.first_link = LinkSearch(data, self.title).first_link()
                if self.first_link:
                    self.first_link = self.first_link
                    logger.debug('First Link: ' + self.first_link)
                    self.last_tag = None
                else:
                    logger.debug("NO LINK!")
        
        def end_element(name):
            if self.title and self.first_link and name == 'page' and (special or ':' not in self.title):
                links = self.links
                if self.is_redirect:
                    links = self.redirects
                if self.title in links:
                    if self.first_link != links[self.title]:
                        logger.warning("Encountered title '" + self.title + "' multiple times.")
                        logger.warning(links[self.title])
                        logger.warning(self.first_link)
                links[self.title] = self.first_link

                logger.debug('Title: ' + repr(self.title) + ' Link: ' + repr(self.first_link))
            if name == 'page':
                self.title = None
                self.fist_link = None
                self.is_redirect = False
            self.last_tag = None

        parser = expat.ParserCreate()

        parser.StartElementHandler = start_element
        parser.EndElementHandler = end_element
        parser.CharacterDataHandler = char_data
        parser.buffer_text = True
        parser.buffer_size = 1000000

        self.parser = parser

    def parse(self):
        """ Execute the parser and correct redirects """
        self.parser.ParseFile(self.xml)

        for key in self.links:
            while self.links[key] in self.redirects:
                self.links[key] = self.redirects[self.links[key]]

        del self.redirects

    def walk(self, page, visited=None):
        """ Debugging function, show path traversed """
        print("Visiting ", repr(page))

        if not visited:
            visited = set()

        if page in visited:
            return

        visited.add(page)

        if page in self.links:
            self.walk(self.links[page], visited)
