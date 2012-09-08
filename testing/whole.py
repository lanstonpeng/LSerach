import urllib2

def get_page(url):
    try:
        return urllib2.urllopen(url).read()
    except:
        return ""

def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url,end_quote

def union(p,q):
    for e in  q:
        if e not in q:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page= page[endpos:]
        else:
            break
    return links

def add_to_index(index,keyword,url):
    '''
    for entry in index:
        if (entry[0] == keyword) and (url not in entry[1]):
            entry[1].append(url)
            return
    index.append([keyword],[url]])
    '''
    if keyword in index:
        if url not in index[keyword] :
            index[keyword].append(url)
    else :
        index[keyword] = [url]

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

def look_up(index,keyword):
    '''
    for entry in index:
        if entry[0] == keyword :
            return entry[1]
    '''
    if keyword in index:
        return index[keyword]
    else:
        return None

def hash_string(keyword,buckets):
    h = 0
    for c in keyword:
        h+=ord(c)
    return h % buckets

def hastable_add(htable,key,value):
    bucket = hashtable_get_bucket(table,key)
    bucket.append([key,value])

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket :
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key,value])

def hashtable_get_bucket(htable,key):
    return htable[ hastable_string(key,len( htable )) ]

def hashtable_lookup(htable,key):
    bucket = hashtabl_get_bucket(htable,key)
    for entry in bucket :
        if entry[0] == key
            return entry[1]
    return None

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled= []
    index = {}
    graph = {}
    while tocrawl and len(crawled) < max_pages :
        page = tocrawl.pop()
        if page not in crawled :
            content = get_page(page)
            add_page_to_index(index,page,content)
            outlinks = get_all_links( get_page(page) )
            graph[page] = outlinks
            union(tocrawl,outlinks)
            crawled.append(page)
    return index,graph
