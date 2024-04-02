from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.single_line_comment = False

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
        self.single_line_comment = True

    def handle_data(self, data):
        if data.strip() and not self.single_line_comment:
            print(">>> Data")
            print(data.strip())
            self.single_line_comment = False

if __name__ == "__main__":
    n = int(input().strip())
    html_code = ""
    for _ in range(n):
        html_code += input().strip()

    parser = MyHTMLParser()
    parser.feed(html_code)
