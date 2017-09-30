import requests
import nltk
from bs4 import BeautifulSoup
import urllib
character_special = ['|', '{', '}', '[', ']', '/', ';', 'var', 'function()', '=', '<', '>', 'a', '@']
def get_content(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.close()
        return r.text  # .encode('utf-8', 'inorge')
    except Exception:
        print('Exception')
        return None

def get_title(url):
    print(url)
    r = get_content(url)
    soup = BeautifulSoup(r, 'html.parser')

    # write to file
    abc = open('home_title.html', 'w')
    abc.write(soup.prettify())
    abc.close()

    # print(soup.get_text())
    # aaa = beautify_string(soup.get_text(),'\n')
    # for d in aaa:
    #     print(d)
    for i in soup.find_all('h1'):
        print(i.get_text())
def beautify_string(str, spl):
    string_array = str.split(spl)
    new_string_array = []
    for sdata in string_array:
        if is_char_special(sdata) == 1 or sdata == '':
            pass
        else:
            new_string_array.append(sdata)

    return (new_string_array)

def is_char_special(sstring):
    for schar in character_special:
        if(sstring.find(schar) != -1):
            return 1

    return 0

if __name__ == "__main__":
    print ("Hello World")
    list_link = []
    for i in range(0, 3):
        temp = get_content('https://www.bing.com/search?q=xây+dựng+hệ+thống+recommendation&first='+(str)(i)+'1&FORM=PERE')
        # abc = open('home'+(str)(i) + '.html', 'w')
        # abc.write(temp)
        # abc.close()
        soup = BeautifulSoup(temp, 'html.parser')
        for i in soup.find_all('h2'):
            for j in i.find_all('a'):
                list_link.append(j['href'])
                # print(j['href'])
    # print(list_link)
    print(len(list_link))

    get_title(list_link[9])

    # file = open('split.txt','r')
    # data = file.read()
    # print(data.find('a'))
    # aaa = beautify_string(data, '\n')
    # for d in aaa:
    #     print(d)