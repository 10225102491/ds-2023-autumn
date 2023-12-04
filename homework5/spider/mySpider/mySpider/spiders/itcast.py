import scrapy
import csv

class ItcastSpider(scrapy.Spider):  # 继承scrapy.spider
    name = 'itcast'
    allowed_domains = ['book.dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.54.00.00.00.00.html']
    for i in range (2,100):
        start_urls.append('http://category.dangdang.com/pg{}-cp01.54.00.00.00.00.html'.format(str(i)))


    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li')
        #print(li_list)
        items = []
        for li in li_list:
            item = {
                "name" : "",
                "price" : "",
            }
            item["name"] = li.xpath('./p[1]/a').extract_first()
            item["price"] = li.xpath('./p[3]/span[1]').extract_first()
            items.append(item)
        for i in items:
            t = i["name"].split('"')
            i["name"] = t[1]
            t = i["price"].split('>')
            t = t[1].split('<')
            i["price"] = t[0]
            print(i)

        with open('books.csv', 'a', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['name','price']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for i in items:
                print(i)
                writer.writerow(i)



