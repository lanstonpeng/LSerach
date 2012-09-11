import re
def visible(element):
    try:
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title',"link"]:
            return False
        return True
    except :
        return False

def filter_text(text):
    return filter(visible,text)
