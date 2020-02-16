from scrapy import cmdline

cmd = 'scrapy crawl logo-and-phone-numbers'
cmdline.execute(cmd.split(' '))