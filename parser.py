#!/usr/bin/python3
import os
import sys
import time
#import requests 
import urllib.request
import threading
from threading import Thread

i=85
exshops = [5,19,21,44,50]
class OpenURL(Thread):
    
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        handle = urllib.request.urlopen(self.url,timeout=3000).read()
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)
	
 
#while i<=50:
#Первый аргумент определяет кол-во магазинов, если не указан по умолчанию выставляется 20
if len(sys.argv)>1:
   nend = sys.argv[1]
else:
   nend = 30
#Второй аргумент определяет кол-во категорий товаров, если не указан по умолчанию выставляется 100
if len(sys.argv)>2:
   iend = sys.argv[2]
else:
   iend = 100
while True:
  urls = []
  n=0
  sid="?id="+str(i)+"&"
  if i not in exshops:
    with open('list.txt', encoding='utf-8') as f: 
       for line in f:
         if sid in line:
           line = line.splitlines()
           urls.extend(line)
           n+=1
         if n>=int(nend):
           break	 
  i+=1
  u=1
  t=0
  threads = []
  if urls:
    for url in urls:
      name = "Thread num: %s" % str(u)
      thread = OpenURL(url, name)
      thread.start()
      threads.append(thread)
      u+=1
    for thread in threads:
       t+=1
       thread.join()
       if t<2:
          break
    threads = []
    #time.sleep(300)
  if i==iend:
     i=1
     print('Start parsing again!')
