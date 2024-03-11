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

### Fundamentals of a Multithreaded Web Crawler:

# 1. **Concurrency**: Multithreading allows the crawler to fetch and process multiple URLs in parallel, making the crawling process faster, especially for I/O-bound tasks like network requests.

# 2. **Task Management**: Using a thread pool (via `ThreadPoolExecutor`), tasks are distributed among multiple threads, which can execute concurrently. This pool also manages the creation and destruction of threads, improving resource utilization.

# 3. **Shared Data**: Threads may share data, such as the set of visited URLs. Proper synchronization is required to prevent race conditions—situations where threads interleave in an undesirable way, leading to incorrect outcomes.

# 4. **URL Filtering**: To avoid crawling the same URL multiple times or leaving the target domain, the crawler checks each new URL against the visited set and the domain name.

# ### Conceptual Example:

# Imagine you're crawling a simple website, starting at `http://example.com/home`. This page contains links to `http://example.com/about` and `http://example.com/contact`.

# 1. **Initialization**: Start with `http://example.com/home`. Initialize the visited set with this URL.

# 2. **Fetching and Processing**:
#     - Fetch `http://example.com/home`. Assume it links to `/about` and `/contact`.
#     - Add these new URLs to a task queue, ensuring they haven't been visited and are within the same domain.

# 3. **Parallel Execution**:
#     - Threads in the pool pick up the tasks: one fetches `/about`, and another fetches `/contact`.
#     - Assume `/about` links back to `/home` and to a new page `/team`.
#     - The thread processing `/about` adds `/team` to the queue (but not `/home`, as it's already visited).

# 4. **Continuation**:
#     - The process continues with threads fetching new URLs from the queue, checking against the visited set, and processing found links.

# 5. **Termination**: The process ends when there are no new URLs to fetch or all active fetches are complete.

# ### Different Example Walkthrough:

# Let's consider another website, `http://example.com/main`, with the following structure:

# - `/main` links to `/products` and `/blog`.
# - `/products` links to `/product_1` and `/main`.
# - `/blog` links to `/article1` and `/external`.

# Using a multithreaded crawler:

# 1. Start at `/main`, marking it as visited.
# 2. Fetch `/main`, discovering links to `/products` and `/blog`. Queue them up for fetching.
# 3. Two threads concurrently process `/products` and `/blog`.
#    - `/products` fetch reveals links to `/product_1` (queued) and `/main` (ignored as visited).
#    - `/blog` fetch reveals links to `/article1` (queued) and `/external` (ignored if it's outside the domain).
# 4. The process continues, with new threads fetching `/product_1` and `/article1`.

# Through this approach, the crawler efficiently navigates the site, respecting domain boundaries and avoiding redundant fetches, all while leveraging the concurrency offered by multithreading to accelerate the crawling process.
# host = 'http://'+startUrl.split('/')[2]
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # Extract the hostname from the starting URL to ensure we only follow internal links.
        host_name = urlparse(startUrl).hostname
        
        # Initialize a set for visited URLs to avoid re-crawling the same pages.
        visited = set([startUrl])
        
        # Initialize a list to store the results, i.e., all crawled URLs.
        result = []
        
        # Initialize a ThreadPoolExecutor to manage a pool of threads.
        # max_workers defines the maximum number of threads that can run concurrently.
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Create an initial set of future tasks. Start by fetching URLs from the startUrl.
            tasks = {executor.submit(htmlParser.getUrls, startUrl)}
            
            # Continue processing as long as there are pending tasks.
            while tasks:
                # as_completed() provides an iterator that yields futures as they complete.
                done = set(as_completed(tasks))
                
                # Remove the completed tasks from the tasks set.
                tasks.difference_update(done)
                
                # Iterate through the completed futures.
                for future in done:
                    # Iterate through URLs fetched by the HtmlParser for a given page.
                    for url in future.result():
                        # Check if the URL has not been visited and belongs to the same host.
                        if url not in visited and urlparse(url).hostname == host_name:
                            # Mark the URL as visited.
                            visited.add(url)
                            # Add a new task to fetch URLs from this newly discovered page.
                            tasks.add(executor.submit(htmlParser.getUrls, url))
                            # Add the URL to the result list.
                            result.append(url)
        
        # Return the list of crawled URLs, starting with the initial URL.
        return [startUrl] + result


        