import gui
import fetcher
import parser_page


def onUrl(url):
    page_fetcher = fetcher.getPage(url)
    page_parser = parser_page.getParser(page_fetcher)
    keyworwds = parser_page.getKeywords(page_parser)
    if keyworwds is not False:
        statistics = parser_page.getStats(page_parser, keyworwds)
    else:
        statistics = "Page does not contain keywords"
    return statistics


gui.startGUI(onUrl)