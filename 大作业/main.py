import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt


def getHTMLText(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    return html

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='cont_l in')
    data = table.find_all('dl')
    for tr in data:
        t = tr.find_all('dt')
        d1 = t[0].text.strip()
        t = tr.find_all('li')
        d2 = t[0].text.strip()
        d3 = t[2].text.strip()
        d4 = t[4].text.strip()
        ulist.append([d1,d2[6:],d3[5:],d4[5:]])

def printUnivList(ulist):
    file_name = "大学.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["大学名称", "大学所在地","大学类型","大学性质"])
        for u in ulist:
            writer.writerow(u)

# 饼图
def generatePieChart(ulist):
    kinds = {}
    for i in ulist:
        kind = i[2]
        if kind == '未知':
            continue
        if kind  in kinds:
            kinds[kind ] += 1
        else:
            kinds[kind ] = 1

    labels = kinds.keys()
    sizes = kinds.values()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(dpi=300)  # 设置图像分辨率为300
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('大学类型分布')
    plt.show()

# 柱形图
def printUnivList2(ulist):
    locations = {}
    for i in ulist:
        location = i[3]
        if location == '未知':
            continue
        if location in locations:
            locations[location] += 1
        else:
            locations[location] = 1

    plt.rcParams['font.sans-serif'] = ['SimHei']
    loc = locations.keys()
    num = locations.values()
    plt.figure(dpi=300)  # 设置图像分辨率为300
    plt.bar(loc, num)
    plt.xlabel('大学性质')
    plt.ylabel('数量')
    plt.title('大学性质分布')
    plt.show()

def main():
    ulist = []
    url = ['http://college.gaokao.com/schlist/p{}'.format(str(i)) for i in range(1,107)]#107
    for i in url:
        html = getHTMLText(i)
        if html is not None:
            fillUnivList(ulist, html)
    for i in range(len(ulist)):
        for j in range(4):
            if ulist[i][j] == '------' or ulist[i][j] == '――':
                ulist[i][j] = '未知'
    #print(ulist)
    printUnivList(ulist)
    printUnivList2(ulist)  # 柱形图
    generatePieChart(ulist)  # 饼图

main()