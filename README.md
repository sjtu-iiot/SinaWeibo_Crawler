IIOT SinaWeibo Crawler
======================

This repository designing a sina weibo crawler is dedicated to research programs of
[IIOT,SJTU](http://iiot.sjtu.edu.cn/)

=======

#Requirements:

* Scrapy >= 0.14
* redis-py (tested on 2.4.9)
* redis server (tested on 2.4-2.6)
* BeautifulSoup 
* pymongo 


# Installation
    $ sudo apt-get install redis-server
    $ sudo pip install requirements.txt


### SinaWeibo Crawler
1. 微博模拟登录

2. 分布式/多线程抓取框架

3. **抓取任务**接口(用户资料/朋友网/微博内容等)

4. 页面内容解析

5. 数据存储（Redis/MongoDB）






### IIOT SinaWeibo Crawler Provides
1. WEIBO Login Simulator

2. Distributed/Multi-Threading Extraction Framework

3. **Extraction Task** Interface(user profile/social network/weibos etc.)

4. Weibo Page Parser

4. Data Storage(Redis/MongoDB)






### How to Use IIOT SinaWeibo Crawler
First config your SinaWeibo Login Account in file "weibocrawler/settings.py"
```
# sina_weibo login account Config
WEIBO_USER_NAME        =    ""
WEIBO_USER_PASSWORD    =    ""
```

under current directory (containing scrapy.cfg), run command:
```
$ scrapy crawl weibospider
```
