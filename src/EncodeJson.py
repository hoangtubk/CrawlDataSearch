import base64
import os, fnmatch
class EncodeJson():
    """A simple class"""
    def __init__(self):
        self.url = ''
        self.title = ''
        self.description = ''
        self.content = ''
        self.relevance = ''

        self.collection = []
        self.sites = []

    def read_file_result(self, path):
        """get url, title, content and relevance of file result
        :param path file result
        :return site : list contain url, title, content and relevance
        """

        file = open(path, "r")
        have_content = False
        lines = file.readlines()
        site = []
        for line in lines:
            if(line == "\n"):
                continue
            if(line.find('|') != -1):
                X = line.split('|')
                if X[0].strip() == 'url' or X[0].strip() == 'URL':
                    url_ = X[1].strip()
                    have_content == False
                if X[0].strip() == 'title' or X[0].strip() == 'Title':
                    title_ = X[1].strip()
                    have_content == False
                if X[0].strip() == 'Content' or X[0].strip() =='content':
                    content_ = X[1].strip()
                    have_content = True
                if X[0].strip() == 'boolean' or X[0].strip() == 'Boolean':
                    relevance_ = X[1].strip()
                    have_content == False
            else:
                if(have_content):
                    content_ = content_ + '\n' + line.strip()
        site.append(url_)
        site.append(title_)
        site.append(content_)
        if relevance_ == 'true' or "True" or 'TRUE':
            site.append('1')
        else:
            site.append('0')

        # print(site)
        return site
    def find_file(self, path_folder):
        """Find all file in path_folder
        :param path_folder path of folder
        :return result file result
        """
        pattern = '*.txt'
        result = []
        for root, dirs, files in os.walk(path_folder):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    def dump_json(self, query, description, path_result):
        """
        :param query: input query
        :param description: description of query
        :param path_result: folder contains result query
        :return: collection : list result 1 query
        """
        collection = []
        collection.append(query)
        collection.append(description)
        paths = self.find_file(path_result)
        sites = []
        for path in paths:
            # print(path)
            sites.append(self.read_file_result(path))
        collection.append(sites)
        return collection

    def creat_file_json(self,query, description, folder_path):
        """
        Create file json from query, description of query and list result
        :param query:
        :param description:
        :param folder_path:
        :return: file json
        """
        data = self.dump_json(query, description, folder_path)
        file_json = '{"collection":[{"query": ' + '\"' + data[0] + '\"' \
                    + ',"description": ' + '\"' + data[1] + '\"' \
                    + ',"sites": ['
        list_site = []
        for i in range(0, len(data[2])):
            content = base64.b64encode(bytes(data[2][i][2], 'utf-8'))
            site = ''
            if i != 0:
                site = site + ','
            site = site + '{"url": ' + '\"' + data[2][i][0] + '\"'  # url
            site = site + ',"title": ' + '\"' + data[2][i][1] + '\"'  # title
            site = site + ',"content": ' + '\"' + (str)(content) + '\"'  # content
            site = site + ',"relevance": ' + '\"' + data[2][i][3] + '\"'   # relevance
            site = site + '}'
            list_site.append(site)

        for i in range(0, len(data[2])):
            file_json = file_json + list_site[i]

        file_json = file_json + ']}]}'
        return (file_json)

if __name__ == "__main__":
    cat = EncodeJson()
    query1 = 'Xây dựng hệ thống recommendation'
    des1 = 'Tìm hiểu được cách thức xây dựng một hệ thống gợi ý cơ bản sử dụng các phương pháp học máy đã được ứng dụng trong các hệ thống thực tế'
    path1 = '/home/tuhoangbk/20171/TK&TDTT/Data/Query 1'

    query2 = 'học deeplearning cơ bản'
    des2 = 'Tìm hiểu các tài liệu hoặc khóa học về deeplearning cơ bản'
    path2 = '/home/tuhoangbk/20171/TK&TDTT/Data/Query 2'

    json1 = cat.creat_file_json(query1, des1, path1)
    json2 = cat.creat_file_json(query2, des2, path2)

    print(json1)
    j1 = open('./json/query1.json', 'w')
    j1.write(json1)
    j1.close()
    print(json2)
    j2 = open('./json/query2.json', 'w')
    j2.write(json2)
    j2.close()