#!/usr/bin/python3
import os
import sys
import time
#import requests 
import urllib.request
import threading
from threading import Thread

i=1
exshops = [5,19,21,44,55]
class OpenURL(Thread):
    
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        handle = urllib.request.urlopen(self.url,timeout=3000).read()
        #handle = requests.get(self.url)
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)
 
#Первый аргумент определяет кол-во магазинов, если не указан по умолчанию выставляется 20
if len(sys.argv)>1:
   nend = sys.argv[1]
else:
   nend = 20
while True:
  urls = []
  n=0
  if i in exshops:
    sid="?id="+str(i)+"&"
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
  if urls:
    for url in urls:
      name = "Thread num: %s" % str(u)
      thread = OpenURL(url, name)
      thread.start()
      u+=1
      time.sleep(300)
    if i==len(exshops):
      i=0
      print('Start parsing again!')
