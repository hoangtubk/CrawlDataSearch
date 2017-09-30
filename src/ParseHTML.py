from bs4 import BeautifulSoup

class ParseHTML(object):
    def __init__(self, raw_content):
        self.raw_content = raw_content
        self.soup = BeautifulSoup(self.raw_content, 'html.parser')

    def get_content_tag(self, tag):
        return self.soup.find_all(tag)

    def get_content_tag_name(self,tag, name):
        return self.soup.find_all_next(tag,name)

if __name__ == "__main__":
    print("Hello World")
    file = open('home.html','r')
    data = file.read()
    file.close()
    soup = BeautifulSoup(data, 'html.parser')
    for i in soup.find_all('h2'):
        for j in i.find_all('a'):
            print(j['href'])
