#!/usr/bin/env bash
source /etc/profile
cd /home/gao/project/WeiboCrawler/WeiboSearch/
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/login.py >> /home/gao/project/WeiboCrawler/WeiboSearch/log/cookie.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/run.py >> /home/gao/project/WeiboCrawler/WeiboSearch/log/bash.log
sleep 3
/home/gao/.pyenv/shims/python /home/gao/project/WeiboCrawler/WeiboSearch/run.py --keyword="冠状病毒" >> /home/gao/project/WeiboCrawler/WeiboSearch/log/bash.log
