def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keywork,[url]])

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

//testing
def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s

def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)

