from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for v in attrs:
            print("->",v[0],">", v[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for v in attrs:
            print("->",v[0],">", v[1])

# input data
N = int(input())
HTML = ""
for s in range(N):
    HTML = HTML + input()

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(HTML)

