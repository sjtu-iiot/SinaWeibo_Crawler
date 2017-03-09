# Scrapy settings for iwctcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
sys.path.append('./misc')

BOT_NAME = 'iwctcrawler'

SPIDER_MODULES    =    ['iwctcrawler.spiders']
NEWSPIDER_MODULE  =     'iwctcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iwctcrawler (+http://www.yourdomain.com)'



# Redis Config
REDIS_HOST   =   "localhost"
REDIS_PORT   =   6379
REDIS_TOCRAWL_QUEUE          =    "user_ids_toCrawl"
REDIS_CRAWLED_QUEUE          =    "user_ids_crawled"
REDIS_PROCESSING_QUEUE       =    "user_ids_processing"
REDIS_PROBLEM_QUEUE          =    "user_ids_problem"



# sina_weibo login account Config
WEIBO_USER_NAME        =    ""
WEIBO_USER_PASSWORD    =    ""


# Item Pipeline
ITEM_PIPELINES   =    [
             'iwctcrawler.pipelines.IwctcrawlerPipeline',
        ]

# Mongodb Config
MONGODB_SERVER             =      'localhost'
MONGODB_PORT               =       27017
MONGODB_DBNAME             =      'sina'
MONGODB_USER_COLLECTION    =      'users'
MONGODB_WEIBO_COLLECTION   =      'weibos'


# schedular config
#SCHEDULER_PERSIST = True
#QUEUE_KEY = '%(spider)s:requests'
#DUPEFILTER_KEY = '%(spider)s:dupefilter'
#SCHEDULER = "iwctcrawler.redis.scheduler.Scheduler"


# Download middlewares Proxy and Agents 
#DOWNLOADER_MIDDLEWARES = {
#        'middlewares.CustomHttpProxyMiddleware':543,
#        'middlewares.CustomUserAgentMiddleware':545,
#        }


# pipelines Config
ITEM_PIPELINES =    ['iwctcrawler.pipelines.IwctcrawlerPipeline']
DOWNLOAD_DELAY =    10
TIME_DELTA     =    30


# bootstrap from file (item.txt) or from db
BOOTSTRAP      =   'file'

FEED_LIMIT     =    300000
