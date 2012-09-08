def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl :
        page =tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl,outlinks )
            crawled.append(page)
    return index
