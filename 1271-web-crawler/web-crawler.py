# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
# from concurrent. futures import ThreadPoolExecutor, as_completed
# class Solution:
#     def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
#         hostname = lambda url:url.split("/")[2]

#         h = hostname(startUrl)
#         print(h)
#         visited = set(startUrl)
#         with ThreadPoolExecutor(max_workers = 10) as ex:
#             d = deque([ex.submit(htmlParser.getUrls, startUrl)])
#             while d and as_completed(d):
#                 current = d.popleft().results()

#                 for url in current:
#                     if url not in visited and hostname(url) == h:
#                         d.append(ex.submit(htmlParser.getUrls, url))
#                         visted.add(url)
#         return list(visited)
from concurrent.futures import ThreadPoolExecutor
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url: str) -> str:
            return url.split('/')[2]

        h = hostname(startUrl)
        visited = set([startUrl])
        with ThreadPoolExecutor(max_workers=10) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                future = tasks.popleft()
                for url in future.result():
                    if url not in visited and hostname(url) == h:
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        return list(visited)



        