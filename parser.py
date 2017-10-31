#!/usr/bin/python3
import os
import time
import requests 
import urllib.request
import threading
from threading import Thread

i=1

class OpenURL(Thread):
    
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        handle = urllib.request.urlopen(self.url).read()
        #handle = requests.get(self.url)
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)
 
#while i<=50:
while True:
  urls = []
  n=0
  sid="?id="+str(i)+"&"
  with open('pars.txt', encoding='utf-8') as f: 
    for line in f:
       if sid in line:
          line = line.splitlines()
          urls.extend(line)
          n+=1
       if n>=19:
          break	 
  i+=1
  #i+=50
  u=1
  for url in urls:
    name = "Thread num: %s" % str(u)
    thread = OpenURL(url, name)
    thread.start()
    u+=1
  time.sleep(600)
  if i==50:
     i=0
     print(Start parsing again!)

