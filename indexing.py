#Indexing
import filterPage
from bs4 import BeautifulSoup
def add_to_index(index,keyword,url):
    if keyword in index:
        if url not in index[keyword] :
            index[keyword].append(url)
    else :
        index[keyword] = [url]

def add_page_to_index(index,url,content):
    try :
        soup = BeautifulSoup(content)
        words = filterPage.filter_text(soup.findAll(text=True))
        for word in words:
            add_to_index(index,word,url)
    except:
        pass

def look_up(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

