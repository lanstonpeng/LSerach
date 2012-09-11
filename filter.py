def visible(element):
    print "-----> ",element,element.parent.name
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True
def filter_text(text):
	return filter(visible,text)
