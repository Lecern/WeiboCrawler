# -*- coding: utf-8 -*-

# Scrapy settings for WeiboSearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiboSearch'

SPIDER_MODULES = ['WeiboSearch.spiders']
NEWSPIDER_MODULE = 'WeiboSearch.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WeiboSearch (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'ALF=1581948724; SCF=AiBSo5vMj6Svv1AXc4yhNwgq2LjJmZZ7NZpEKqziuYN_n3JoQdDR0jQihMmpbX9baD3XnZCJnFXXwdg8c9PCc8A.; SUB=_2A25zJ2PCDeRhGeFN7FYU8CzEwziIHXVQ6A2KrDV6PUJbktANLVXWkW1NQ8h2YCJ46Fd0eMLUFdb6-BNmeW1TVoxZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWCaV8D1oivmPMr11DJ.F_25JpX5K-hUgL.FoM0S0BfehzR1hB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoM4e0-cS02ReK.c; SUHB=0z1QwEai-QCXXR; SSOLoginState=1579357074; _T_WM=5eef7bb3a357c3a4fea15771d2b95bec'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'WeiboSearch.middlewares.WeibosearchSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'WeiboSearch.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'WeiboSearch.middlewares.CookiesMiddleware': 554,
    'WeiboSearch.middlewares.ProxyMiddleware': 555,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'WeiboSearch.pipelines.TimePipeline': 300,
    'WeiboSearch.pipelines.WeiboSpiderPipeline': 301,
    'WeiboSearch.pipelines.MongoPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


RETRY_HTTP_CODES = [401, 403, 408, 414, 500, 502, 503, 504]

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'weibo_records'
WEIBO_COLLECTION = 'weibo'
USER_COLLECTION = 'users'


# ip代理 池
PROXY_URL = 'http://127.0.0.1:5000/proxy/target/weibo/cn'

KEY_WORDS = '武汉 肺炎'