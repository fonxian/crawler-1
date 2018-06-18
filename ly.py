# -*- coding: UTF-8 -*-

from urllib import request
import chardet
from bs4 import BeautifulSoup
import requests
import time

    # response = request.urlopen("http://jzsc.mohurd.gov.cn/dataservice/query/comp/list")
    # html = response.read()
    # html = html.decode("utf-8")
    # soup = BeautifulSoup(html,"html.parser")
    #
    # # print(soup.title.string)
    # # print(soup.p.string)
    # # print(soup.find_all('a'))
    # # print(soup.get_text())
    #
    # print("-----------")
    # test = soup.select("body > div.main_box.nav_mtop > div.mtop > table > tbody > tr")
    #
    # for i in test:
    #     print("xxxxxxxxxxxxxxxxxxxxxx")
    #     tdlist = i.find_all("td")
    #     for j in tdlist:
    #         if '企业名称' in str(j):
    #             print("企业名称:"+j.get_text().strip())
    #         if '统一社会信用代码' in str(j):
    #             print("统一社会信用代码:" + j.get_text().strip())
    #         if '企业法定代表人' in str(j):
    #             print("企业法定代表人:" + j.get_text().strip())
    #         if '企业注册属地' in str(j):
    #             print("企业注册属地:" + j.get_text().strip())
    #         # print(j.get_text().strip())
    #     print("xxxxxxxxxxxxxxxxxxxxxx")


def req_all():
    for i in range(2):
        req(i)
        time.sleep(1)

def req(current):
    content = {'$reload': '0', '$pg': current, '$pgsz': '15'}
    res = requests.post('http://jzsc.mohurd.gov.cn/dataservice/query/comp/list', data=content)
    parse(res.text)

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body > div.main_box.nav_mtop > div.mtop > table > tbody > tr")
    for i in test:
        print("xxxxxxxxxxxxxxxxxxxxxx");
        tdlist = i.find_all("td")
        links=[]
        for j in tdlist:
            if '企业名称' in str(j):
                print(j)
                a = j.find_all("a")
                print(a[0]['href'])
                print("企业名称:" + j.get_text().strip())
            if '统一社会信用代码' in str(j):
                print("统一社会信用代码:" + j.get_text().strip())
            if '企业法定代表人' in str(j):
                print("企业法定代表人:" + j.get_text().strip())
            if '企业注册属地' in str(j):
                print("企业注册属地:" + j.get_text().strip())
            # print(j.get_text().strip())
        print("xxxxxxxxxxxxxxxxxxxxxx")
    return


if __name__ == "__main__":
    req_all();
    pass
