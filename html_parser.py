# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1] if attr[1] else "None")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1] if attr[1] else "None")

if __name__ == '__main__':
    n = int(input())
    if n < 100:
        html_code = ""
        for _ in range(n):
            html_code += input().strip()
        parser = MyHTMLParser()
        parser.feed(html_code)
