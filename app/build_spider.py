# -*- coding: UTF-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import requests
import time

from app.build_db import *


def crawl_all():
    i = 1;
    while i <= 1000000:

        if req_list(i) == True:
            i = i + 1
            time.sleep(2)
        else:
            break


# 目标网页 http://jzsc.mohurd.gov.cn

# 请求列表页
def req_list(current):
    print('当前页面数:' + str(current))
    content = {'$reload': '0', '$pg': current, '$pgsz': '15'}
    res = requests.post('http://jzsc.mohurd.gov.cn/dataservice/query/comp/list', data=content)
    if res.status_code == 403:
        print("抓取完毕")
        return False
    parse_list(res.text)
    return True


# 解析列表页
def parse_list(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body > div.main_box.nav_mtop > div.mtop > table > tbody > tr")
    for i in test:
        print("xxxxxxxxxxxxxxxxxxxxxx");
        tdlist = i.find_all("td")

        # 获取详情页主页数据
        for j in tdlist:
            if '企业名称' in str(j):
                print("企业名称:" + j.get_text().strip())
            if '统一社会信用代码' in str(j):
                print("统一社会信用代码:" + j.get_text().strip())
            if '企业法定代表人' in str(j):
                print("企业法定代表人:" + j.get_text().strip())
            if '企业注册属地' in str(j):
                print("企业注册属地:" + j.get_text().strip())
            # print(j.get_text().strip())

        # 获取详情页子页面数据
        for j in tdlist:
            if '企业名称' in str(j):
                a = j.find_all("a")
                # 获取详情Id
                detail_url = a[0]['href']
                detail_str_list = detail_url.split('/')
                detail_id = detail_str_list[-1]
                req_detail_all(detail_id, j.get_text().strip())

        print("xxxxxxxxxxxxxxxxxxxxxx")
    return


# 请求详情页
def req_detail_all(detail_id, company_name):
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compDetail/' + detail_id
    reqa = request.urlopen(url)
    html = reqa.read()
    html = html.decode("utf-8")
    parse_deail_all(html=html, company_id=detail_id, company_name=company_name)

    # 请求企业资格
    req_right()
    # 请求注册人员
    req_register()
    # 请求工程项目
    req_project()
    # 请求良好行为
    req_good()
    # 请求黑名单
    req_black()


# 解析详情页
def parse_deail_all(html, company_id, company_name):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("div.plr table tbody tr")

    credit_code = ''
    company_person = ''
    area = ''
    business_code = ''
    reg_type = ''
    address = ''

    for i in test:
        tds = i.select("td")

        for j in tds:
            if "组织机构代码/营业执照编号" in str(j):
                credit_code = j.get_text().strip()
                print("组织机构代码/营业执照编号：" + j.get_text().strip())
            if "企业法定代表人" in str(j):
                company_person = j.get_text().strip()
                print("企业法定代表人：" + j.get_text().strip())
            if "企业登记注册类型" in str(j):
                reg_type = j.get_text().strip()
                print("企业登记注册类型:" + j.get_text().strip())
            if "企业注册属地" in str(j):
                area = j.get_text().strip()
                print("企业注册属地:" + j.get_text().strip())
            if "企业经营地址" in str(j):
                address = j.get_text().strip()
                print("企业经营地址：" + j.get_text().strip())

    builds = (company_id, credit_code, company_name, company_person, area, reg_type, address)
    save_build_main(builds)


# 请求详情页 - 企业资质资格
def req_right():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/001607230057395100?_=1529592388332'
    reqb = request.urlopen(url)
    html = reqb.read()
    html.decode("utf-8")
    parse_right(html)


# 解析详情页 - 企业资质资格
def parse_right(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("#catabled tbody tr")
    for i in test:
        tds = i.select("td")
        for j in tds:
            if "序号" in str(j):
                print("序号:" + j.get_text().strip())
            if "资质类别" in str(j):
                print("资质类别" + j.get_text().strip())
            if "资质证书号" in str(j):
                print("资质证书号" + j.get_text().strip())
            if "资质名称" in str(j):
                print("资质名称" + j.get_text().strip())
            if "发证日期" in str(j):
                print("发证日期" + j.get_text().strip())
            if "证书有效期" in str(j):
                print("证书有效期" + j.get_text().strip())
            if "发证机关" in str(j):
                print("发证机关" + j.get_text().strip())


# 请求详情页 - 注册人员
def req_register():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/regStaffList/001607220057394803'
    html = request.urlopen(url).read().decode("utf-8")
    parse_register(html)


def parse_register(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body table tbody tr")
    for i in test:
        tds = i.select("td")
        print("----------------")
        for j in tds:
            if "身份证号" in str(j):
                print("身份证号:" + j.get_text().strip())
            if "注册类别" in str(j):
                print("注册类别:" + j.get_text().strip())
            if "注册号" in str(j):
                print("注册号（执业印章号）:" + j.get_text().strip())
            if "注册专业" in str(j):
                print("注册专业:" + j.get_text().strip())
        print("----------------")


# 请求详情页 - 工程项目
def req_project():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/001607220057358999'
    html = request.urlopen(url).read().decode("utf-8")
    parse_project(html)


# 解析详情页 - 工程项目
def parse_project(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body table tbody tr")
    for i in test:
        tds = i.select("td")
        print("----------------")
        for j in tds:
            if "项目编码" in str(j):
                print("项目编码:" + j.get_text().strip())
            if "项目名称" in str(j):
                print("项目名称:" + j.get_text().strip())
            if "项目属地" in str(j):
                print("项目属地:" + j.get_text().strip())
            if "项目类别" in str(j):
                print("项目类别:" + j.get_text().strip())
            if "建设单位" in str(j):
                print("建设单位:" + j.get_text().strip())
        print("----------------")


# 请求详情页 - 良好行为
def req_good():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/001607220057358999'
    html = request.urlopen(url).read().decode("utf-8")
    parse_project(html)


# 解析详情页 - 良好行为
def parse_good(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body table tbody tr")
    for i in test:
        tds = i.select("td")
        print("----------------")
        for j in tds:
            if "项目编码" in str(j):
                print("项目编码:" + j.get_text().strip())
            if "项目名称" in str(j):
                print("项目名称:" + j.get_text().strip())
            if "项目属地" in str(j):
                print("项目属地:" + j.get_text().strip())
            if "项目类别" in str(j):
                print("项目类别:" + j.get_text().strip())
            if "建设单位" in str(j):
                print("建设单位:" + j.get_text().strip())
        print("----------------")


# 请求详情页 - 黑名单记录
def req_black():
    url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compCreditBlackList/001607220057214285'
    html = request.urlopen(url).read().decode("utf-8")
    parse_project(html)


# 解析详情页 - 黑名单记录
def parse_black(html):
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select("body table tbody tr")
    for i in test:
        tds = i.select("td")
        print("----------------")
        for j in tds:
            if "黑名单记录主体" in str(j):
                print("黑名单记录主体:" + j.get_text().strip())
            if "黑名单认定依据" in str(j):
                print("黑名单认定依据:" + j.get_text().strip())
            if "认定部门" in str(j):
                print("认定部门:" + j.get_text().strip())
            if "列入黑名单日期" in str(j):
                print("列入黑名单日期:" + j.get_text().strip())
            if "移出黑名单日期" in str(j):
                print("移出黑名单日期:" + j.get_text().strip())
        print("----------------")


# 请求详情页 - 变更记录
def req_change():
    pass

    # http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/001607230057395100?_=1529328120435

    # http: // jzsc.mohurd.gov.cn / dataservice / query / comp / regStaffList / 001607230057395100

    # http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/001607230057395100

    # http://jzsc.mohurd.gov.cn/dataservice/query/comp/compCreditRecordList/001607230057395100/0

    # http://jzsc.mohurd.gov.cn/dataservice/query/comp/compCreditRecordList/001607230057395100/1


def save_build_main(builds):
    args = (builds[0], builds[1], builds[2], builds[3], builds[4], builds[5], builds[6])
    insert_build_main(*args)


# if __name__ == "__main__":
#     crawl_all()
#     # b()
#     # c()
#     # req_register()
#     # req_project()
#     pass
