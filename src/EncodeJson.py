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
                if X[0].lower().find('url') != -1:
                    url_ = X[1].strip()
                    have_content == False
                if X[0].strip().lower() == 'title':
                    title_ = X[1].strip()
                    have_content == False
                if X[0].strip().lower() == 'content':
                    content_ = X[1].strip()
                    have_content = True
                if X[0].strip().lower() == 'boolean':
                    relevance_ = X[1].strip()
                    have_content == False
            else:
                if(have_content):
                    content_ = content_ + '...' + line.strip()
        site.append(url_)
        title_ = title_.replace("\"", "")
        title_ = title_.replace("\'", "")
        # title_ = title_.replace("\\", "")

        site.append(title_)
        content_ = content_.replace("\"", "")
        content_ = content_.replace("\'", "")
        # content_ = content_.replace("\\", "")
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
            #don't use base64
            content = data[2][i][2]
            #use base64
            # content = base64.b64encode(bytes(data[2][i][2], 'utf-8'))
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
    path1 = '../Data/Query 1'

    query2 = 'học deeplearning cơ bản'
    des2 = 'Tìm hiểu các tài liệu hoặc khóa học về deeplearning cơ bản'
    path2 = '../Data/Query 2'

    query3 = 'Giải thuật di truyền'
    des3 = 'Tìm hiểu về giải thuật di truyền và các bài toán liên quan đến giải thuật di truyền'
    path3 = '../Data/Query 3'

    query4 = 'suy diễn tiến'
    des4 = 'Tìm hiểu về suy diễn tiến và các bài toán về suy diễn tiến'
    path4 = '../Data/Query 4'

    query5 = 'giải thuật SVM'
    des5 = 'Tìm hiểu về phương pháp học máy SVM và các bài toán ứng dụng của nó'
    path5 = '../Data/Query 5'

    query6 = 'phương pháp trọng số tf-idf'
    des6 = 'Tìm hiểu về phương pháp đánh trọng số tf-idf cho văn bản'
    path6 = '../Data/Query 6'

    json1 = cat.creat_file_json(query1, des1, path1)
    json2 = cat.creat_file_json(query2, des2, path2)
    json3 = cat.creat_file_json(query3, des3, path3)
    json4 = cat.creat_file_json(query4, des4, path4)
    json5 = cat.creat_file_json(query5, des5, path5)
    json6 = cat.creat_file_json(query6, des6, path6)

    print(json1)
    j1 = open('./json/query1.json', 'w')
    j1.write(json1)
    j1.close()
    # print(json2)
    j2 = open('./json/query2.json', 'w')
    j2.write(json2)
    j2.close()
    # print(json3)
    j3 = open('./json/query3.json', 'w')
    j3.write(json3)
    j3.close()
    # print(json4)
    j4 = open('./json/query4.json', 'w')
    j4.write(json4)
    j4.close()
    # print(json5)
    j5 = open('./json/query5.json', 'w')
    j5.write(json5)
    j5.close()
    # print(json6)
    j6 = open('./json/query6.json', 'w')
    j6.write(json6)
    j6.close()