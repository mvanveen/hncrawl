import hashlib
import json
import os

from beautiful_soup import BeautifulSoup as bs
from scrapy.http import Request
from scrapy.spider import BaseSpider
from news.items import NewsItem

PATH = '/Users/mvanveen/root/dev/news/out/'

class HnspiderSpider(BaseSpider):
  name = 'hnspider'
  allowed_domains = []
  start_urls = ['http://news.ycombinator.com']

  def parse(self, response):
    if 'news.ycombinator.com' in response.url:
      soup = bs(response.body)
      items = [(x[0].text, x[0].get('href')) for x in
        filter(None, [
          x.findChildren() for x in
            soup.findAll('td', {'class':'title'})
        ])]

      for item in items:
        print item
        news_item = NewsItem()
        news_item['title']  = item[0]
        news_item['url']    = item[1]
        try:
          yield Request(item[1], callback=self.parse)
        except ValueError:
          yield Request('http://news.ycombinator.com/' + item[1], callback=self.parse)

        yield news_item

    else:
      sha1_response = hashlib.sha1(response.url).hexdigest()
      if not os.path.exists(PATH + sha1_response):
        os.makedirs(PATH + sha1_response)
      with open(PATH + sha1_response + '/html', 'w+') as file_obj:
        file_obj.write(response.body)
