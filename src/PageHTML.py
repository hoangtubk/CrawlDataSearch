import base64
import requests
import nltk
from bs4 import BeautifulSoup
import urllib
character_special = ['{', '}', '[', ']', '/', ';', 'var', 'function()', '=', '<', '>', 'a', '@']
def get_content(url):
    """
    Lay noi dung html cua moi trang chu search
    :param url: url vd:bing.com/search?q=abcxyz
    :return: Noi dung dang html
    """
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.close()
        return r.text  # .encode('utf-8', 'inorge')
    except Exception:
        print('Exception')
        return None

def get_title(url):
    """
    Lay phan title cua trang web
    :param url: duong dan cua website
    :return: noi dung cua title
    """
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
        return (i.get_text())
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
    """
    Kiem tra co phai ki tu dac biet khong
    :param sstring: ki tu can kiem tra
    :return: true neu dung va nguoc lai
    """
    for schar in character_special:
        if(sstring.find(schar) != -1):
            return 1

    return 0

if __name__ == "__main__":
    print ("Hello World")
    list_link = []
    for i in range(0, 3):
        # temp = get_content('https://www.bing.com/search?q=xây+dựng+hệ+thống+recommendation&first=' + (str)(i) + '1&FORM=PERE')
        # temp = get_content('https://www.bing.com/search?q=học+deeplearning+cơ+bản&first=' + (str)(i) + '1&FORM=PERE')
        # temp = get_content('https://www.bing.com/search?q=giải+thuật+di+truyền&first=' + (str)(i) + '1&FORM=PERE')
        temp = get_content('https://www.bing.com/search?q=suy+diễn+tiến&first=' + (str)(i) + '1&FORM=PERE')
        soup = BeautifulSoup(temp, 'html.parser')
        # Doi voi moi trang, tinh
        for i in soup.find_all('h2'):
            for j in i.find_all('a'):
                list_link.append(j['href'])
                # print(j['href'])

    for i in range(0, len(list_link)):
        title = get_title(list_link[i])

        content = get_content(list_link[i])
        cleantext = BeautifulSoup(content).text

        #maxclean tra ve mot mang
        maxclean = beautify_string(cleantext, '\n')

        file = open('./Q4/' + (str)(i) +'.txt', 'a')
        file.write((str)(list_link[i]) + '\n')
        file.write((str)(title) + '\n')
        for line in range(0,len(maxclean)):
            file.write(maxclean[line])
            file.write('\n')
        file.close()