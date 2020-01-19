from scrapy import cmdline
cmdline.execute('scrapy crawl weibo_spider -s LOG_ENABLED=0'.split())