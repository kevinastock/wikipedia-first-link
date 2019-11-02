"""Analyze graph of first links"""

from collections import deque

import logging
logger = logging.getLogger(__name__)

class WikiAnalysis:
    def __init__(self, links):
        self.graph = {}
        self.pages = len(links)
        self.links = links
        self.visitor_stats = {}

        for src in links:
            dest = links[src]
            if dest in self.graph:
                self.graph[dest].append(src)
            else:
                self.graph[dest] = [src]

        logger.info("Total pages: " + str(self.pages))
        logger.info("Nodes in graph: " + str(len(self.graph)))

    def find_end(self, page, visited=None):
        """ Report the last page visited when following first links 
        from 'page' """
        logger.debug("'end' Visiting " + repr(page))

        if visited is None:
            visited = set()

        if page in visited or page not in self.links or not self.links[page]:
            return page

        visited.add(page)
        return self.find_end(self.links[page], visited)
    
    def all_ends(self):
        """ Find all end pages/cycles """
        ends = set()
        for page in self.links:
            ends.add(self.find_end(page))

        ret = []
        while ends:
            page = ends.pop()
            pages = set()
            """ Get cycle with find_end """
            self.find_end(page, pages)
            pages.add(page)

            """ Remove all pages in the cycle from ends """
            for page in pages:
                if page in ends:
                    ends.remove(page)

            ret += [pages]

        if self.visitor_stats:
            def first(x):
                for e in x:
                    return e
            ret.sort(key=lambda x: self.visitor_stats[first(x)][1], reverse=True)
            ret = [self.visitor_stats[first(pages)][0] + ' ' + ', '.join(pages) for pages in ret]
        else:
            ret.sort(key=len)

        return ret

    def visitors_bfs(self, page):
        """ Count the number of pages that visit 'page' """
        logger.debug("BFS visiting " + repr(page))

        visited = {page:0}
        queue = deque([page])

        while queue:
            page = queue.popleft()
            dist = visited[page]
            if page in self.graph:
                for link in self.graph[page]:
                    if link not in visited:
                        visited[link] = dist + 1
                        queue.append(link)

        avg_clicks = sum(visited.values())/len(visited)
        most_clicks = max(visited.values())
        pages_at_most = [x for x in visited if visited[x] == most_clicks]
        return ["%.2f" % (100 * len(visited)/self.pages), len(visited), avg_clicks, most_clicks, pages_at_most]
    
    def all_visitors(self):
        """ Array of stats for how much each page is reached """
        results = []
        for page in self.graph:
            stats = self.visitors_bfs(page)
            results.append(stats + [page])
            self.visitor_stats[page] = stats
        results.sort(key=lambda x: x[1:], reverse=True)
        return results
