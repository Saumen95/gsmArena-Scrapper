import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gsmarena.items import GsmarenaItem


class GsmArenaSpider(CrawlSpider):
    name = 'gsmarena'
    allowed_domains = ['gsmarena.com']
    start_urls = ['https://www.gsmarena.com/']
    rules = (
        Rule(LinkExtractor(allow=('/[a-z0-9_\-]+-reviews-\d+.php',)), callback='parse_phone', follow=True),
    )

    def parse_phone(self, response):
        item = GsmarenaItem()
        item['name'] = response.url.split('/')[-1].split('-')[0]
        item['specs'] = response.xpath('//div[@class="specs"]/p/text()').extract()
        yield item


