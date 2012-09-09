import urllib2,requests
from bs4 import BeautifulSoup

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled= []
    index = {}
    graph = {}
    while tocrawl and len(crawled) < max_pages :
        page = tocrawl.pop()
        if page not in crawled :
            content = get_page(page)
            #add_page_to_index(index,page,content)
            outlinks = get_all_links( content ,page)
            #graph[page] = outlinks
           
            union(tocrawl,outlinks)
            print "------------------------",tocrawl
            crawled.append(page)
    #return index,graph
    return crawled

def union(p,q):
    for e in  q:
        print e
        if e not in p:
            print "yep"
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
    for link in soup.findAll("a"):
        url = link.get("href")
        if url.find("http") < 0 :
            url = parentURL + url
        result.append(url)
    return result

print crawl_web('http://www.baidu.com',10)


