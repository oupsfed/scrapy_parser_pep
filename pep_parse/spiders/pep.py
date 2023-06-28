import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_table = response.css('section[id="numerical-index"]')
        tr_tags = pep_table.css('tr')
        for tr in tr_tags:
            pep_link = tr.css('td + td a::attr(href)').get()
            if pep_link:
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        title = title.split(' – ')
        number = int(title[0][4:])
        name = title[1]
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
