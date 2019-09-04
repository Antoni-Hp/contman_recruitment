import urllib.request

def getPage(url):
    return urllib.request.urlopen(url)
