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


def a():
    for i in range(2):
        reqa(i)
        time.sleep(1)

def reqa(current):
    content = {'$reload': '0', '$pg': current, '$pgsz': '15'}
    res = requests.post('http://jzsc.mohurd.gov.cn/dataservice/query/comp/list', data=content)
    parsea(res.text)

def parsea(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body > div.main_box.nav_mtop > div.mtop > table > tbody > tr")
    for i in test:
        print("xxxxxxxxxxxxxxxxxxxxxx");
        tdlist = i.find_all("td")
        links=[]
        for j in tdlist:
            if '企业名称' in str(j):
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

def b():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compDetail/001607230057395100'
    reqb(url)

def reqb(url):
    reqa = request.urlopen(url)
    html=reqa.read()
    html = html.decode("utf-8")
    parseb(html)

def parseb(html):
    soup = BeautifulSoup(html,"html.parser")
    test = soup.select("div.plr table tbody tr")
    for i in test:
        tds = i.select("td")
        for j in tds:
            if "组织机构代码/营业执照编号" in str(j):
                print("组织机构代码/营业执照编号："+j.get_text().strip())
            if "企业法定代表人" in str(j):
                print("企业法定代表人："+j.get_text().strip())
            if "企业登记注册类型" in str(j):
                print("企业登记注册类型:"+j.get_text().strip())
            if "企业注册属地" in str(j):
                print("企业注册属地:"+j.get_text().strip())
            if "企业经营地址" in str(j):
                print("企业经营地址："+j.get_text().strip())
            print("-------------")

def c():
     url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/001607230057395100?_=1529592388332'
     reqb = request.urlopen(url)
     html = reqb.read()
     html.decode("utf-8")
     parsec(html)


def parsec(html):
    soup = BeautifulSoup(html,"html.parser")
    test = soup.select("#catabled tbody tr")
    for i in test:
        tds = i.select("td")
        for j in tds:
            if "序号" in str(j):
                print("序号:"+j.get_text().strip())
            if "资质类别" in str(j):
                print("资质类别"+j.get_text().strip())
            if "资质证书号" in str(j):
                print("资质证书号"+j.get_text().strip())
            if "资质名称" in str(j):
                print("资质名称"+j.get_text().strip())
            if "发证日期" in str(j):
                print("发证日期"+j.get_text().strip())
            if "证书有效期" in str(j):
                print("证书有效期"+j.get_text().strip())
            if "发证机关" in str(j):
                print("发证机关"+j.get_text().strip())



    #http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/001607230057395100?_=1529328120435

    #http: // jzsc.mohurd.gov.cn / dataservice / query / comp / regStaffList / 001607230057395100

    #http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/001607230057395100

    #http://jzsc.mohurd.gov.cn/dataservice/query/comp/compCreditRecordList/001607230057395100/0

    #http://jzsc.mohurd.gov.cn/dataservice/query/comp/compCreditRecordList/001607230057395100/1

if __name__ == "__main__":
    # a()
    # b()
    c()
    pass

