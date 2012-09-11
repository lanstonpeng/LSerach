import urllib2,requests
from bs4 import BeautifulSoup
import indexing
import filterPage

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled= []
    index = {}
    graph = {}
    while tocrawl and len(crawled) < max_pages :
        page = tocrawl.pop()
        if page not in crawled :
            content = get_page(page)
            indexing.add_page_to_index(index,page,content)
            outlinks = get_all_links( content ,page)
            graph[page] = outlinks
            union(tocrawl,outlinks)
            crawled.append(page)
    return index,graph

def union(p,q):
    for e in  q:
        if e not in p:
            p.append(e)

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        return ""

def get_all_links(content,parentURL):
    soup = BeautifulSoup(content)
    result = []
    for link in soup.findAll(lambda tag: tag.name == "a" and tag.has_key("href")):
        try:
            url = link.get("href")
            if url.find("http") < 0 :
                url = parentURL + url
            result.append(url)
        except:
            pass
    return result

print crawl_web('http://news.ycombinator.com',1)

'''
soup = BeautifulSoup(get_page("http://news.ycombinator.com"))
soup.encode("utf-8")
print filterPage.filter_text( soup.findAll(text=True) )
print BeautifulSoup(get_page("http://www.ifanr.com"),from_encoding="utf-8").findAll(text=True)
'''

