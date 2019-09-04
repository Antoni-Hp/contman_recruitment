from bs4 import BeautifulSoup
import re

def getParser(page):
    return BeautifulSoup(page, 'html.parser')

def getKeywords(page):
    if page.find("meta", {"name": "keywords"}):
        return str(page.find("meta", {"name": "keywords"})['content']).split(',')
    elif page.find("meta", {"name": "Keywords"}):
        return str(page.find("meta", {"name": "Keywords"})['content']).split(',')
    else:
        return False

def getStats(page, keywords):
    key_dict = {}
    for key in keywords:
        key = key.strip()
        k = re.compile(key)
        key_dict[key] = len(k.findall(page.get_text()))
    return key_dict

