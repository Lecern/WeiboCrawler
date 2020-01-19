from scrapy import cmdline
import argparse
from datetime import datetime, timedelta

now_date = datetime.now().strftime("%Y-%m-%d")
one_day_ago = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
two_days_ago = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=str, default=one_day_ago)
parser.add_argument("--end", type=str, default=now_date)
parser.add_argument("--ori", type=bool, default=True)
args = parser.parse_args()

execute = 'scrapy crawl weibo_spider -s LOG_ENABLED=0'
if args:
    execute += ' -a start={} -a end={} -a ori={}'.format(args.start, args.end, args.ori)

cmdline.execute(execute.split())
