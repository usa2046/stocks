#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Author : zhenbei
# @File : currency.py
# @Time : 2020-03-06 13:56

import requests as req
from lxml import etree
url='http://data.eastmoney.com/cjsj/goldforexreserve.aspx?p=1'
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.31 Safari/537.36',
          }
res=req.post(url,headers).text
dt=etree.HTML(res)
infos=dt.xpath('//*[@id="tb"]/tr')
for i in range(1,len(infos)):
