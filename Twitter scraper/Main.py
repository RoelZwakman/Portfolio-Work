import sys
import urllib.request
from bs4 import BeautifulSoup

class twitter_searcher():
    def __init__(self):
        self.searchable_tags = ("div", "span", "li")

    def getSearch(self, search_query):
        """Gets the HTML code as a string from the twitter search page for search_query"""

        request = urllib.request.urlopen(f'http://twitter.com/search?f=tweets&vertical=news&q={search_query}&src=typd')
        html_as_bytes = request.read()
        html_as_string = html_as_bytes.decode("utf8")
        request.close()
        return html_as_string

    def parseSearch(self, html, tag_to_search):
        """Parses through unfiltered HTML in string-format and returns it parsed."""

        soup = BeautifulSoup(html, features="html.parser")
        if tag_to_search in self.searchable_tags:
            tag_results = soup.findAll(tag_to_search)
            return tag_results
        else:
            return None

    def outputSearch(self, parsedResults):
        """Prints parsedResults to the screen with dividers above and below."""

        self.printDivider()
        print(parsedResults)
        self.printDivider()

    def printDivider(self):
        """Prints a line divider to the screen."""

        print("-----------------------------------------------------------------")


def main():

    twitsearch = twitter_searcher()

    search_term = sys.argv[1]
    tag_to_search = sys.argv[2]
    output_unparsed = twitsearch.getSearch(search_term)
    output_parsed = twitsearch.parseSearch(output_unparsed, tag_to_search)

    if output_parsed == None:
        print("The provided HTML-tag was not found on the page, or was not a searchable tag.")
    else:
        twitsearch.outputSearch(output_parsed)

main()