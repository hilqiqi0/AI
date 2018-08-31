# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'tencent'
    # 这里用来防止抓取数据时跳转到其他域名的网站
    allowed_domains = ['hr.tencent.com']
    
    # seed url种子URL
    #start_urls = ['https://hr.tencent.com/position.php?keywords=python']
#第一种翻页的方法：一次性的把所有的URL取出来，
#放到start_urls中去
#    start_urls = []
#    for i in range(0,540,10):
#        url = "https://hr.tencent.com/position.php?keywords=python&start="+str(i)+"#a"
#        start_urls.append(url)

#第二种翻页的方法：首先给一个seed url作为开始点
#在每一次parse时，通过得到的response取出下一个url，
#发起下一次request请求
    url = "https://hr.tencent.com/position.php?keywords=python&start="
    offset = 0
    start_urls = [url+str(offset)+"#a"]

    # 每次获取response响应时会调用这个方法，
    #需要在这个地方精确的匹配信息
    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentspiderItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = "https://hr.tencent.com/"+each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            yield item #返回给pipelines process_item
            
        # 翻页的第二种方法
        #这里最好的做法还是从response中把下一页的url取出来
        if self.offset < 540:
            self.offset += 10
            nextPageUrl = self.url+str(self.offset)+"#a"
        else:
            return
        # 对下一页发起request请求，指定一个回调方法
        yield scrapy.Request(nextPageUrl, callback=self.parse)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
