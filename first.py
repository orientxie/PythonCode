import requests
from bs4 import BeautifulSoup
import numpy
import csv
def get_html(html,keywords=None):
    try:
        heade = {
            'User-Agent':
                'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
        }
        wb = requests.get(html, headers=heade)
        wb.encoding = wb.apparent_encoding
        if wb.status_code==200:
            return wb.text
        return "获取失败"
    except Exception as error:
        print(error)
        return "请求发生错误"

def parse(html):
    soup=BeautifulSoup(html,"lxml")
    rows=soup.select("tr")
    retls=[]
    for row in rows:
        row= row.select("td")
        templs=[]
        for col in row:
            templs.append(col.text)
        retls.append(templs)
        print(templs)
    return retls

def sace_svc(list):
    f = open('大学排名.csv', 'w', newline='')
    writer = csv.writer(f)
    for i in list:
        writer.writerow(i)
    f.close()
html =get_html("http://www.bspider.top/gaosan/")
list=parse(html)
sace_svc(list)