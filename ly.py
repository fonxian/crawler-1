# -*- coding: UTF-8 -*-

from urllib import request


if __name__ == "__main__":
    response = request.urlopen("http://jzsc.mohurd.gov.cn/dataservice/query/comp/list")
    html = response.read()
    html = html.decode("utf-8")
    print(html)
    print("方志杰是只猪")

   



