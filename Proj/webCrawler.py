import urllib2,requests

def get_page(_asUrl):
    if _asUrl.find("http://") < 0 :
        _asUrl = "http://"+ _asUrl
    _oRequest = requests.get(_asUrl)
    if _oRequest.status_code == 200 :
        _sContent = _oRequest.text
        return _sContent


result = get_page("lanstonpeng.blogcn.com")
print result.find("http://",100)
print result[136:150]

def crawl_web([_asSeed]):
    _oToCrawl = [_asSeed]
    _oCrawled = []
    for _sItem in (_oToCrawl):
        _sResult = get_page(_sItem)
        _oCrawled.append(_oToCrawl.pop())

        match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)



