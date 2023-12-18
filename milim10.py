#import webbrowser
#url = "https://#www.youtube.com/"
#print (webbrowser.get()) 
# chrome
#webbrowser.open(url)
#webbrowser.open_new(url)
#webbrowser.open_new_tab(url)
#from urllib2 
from __future__ import absolute_import
from __future__ import print_function
import urlopen
import webbrowser
u=urlopen("https://python.org")
#url=("https://python.org")
#u=url
#print (webbrowser.get()):
#webbrowser.open_new(u)

words={}
for line in u:
    line = line.strip(" \n")
    for word in line.split(" "):
        try:
            words[word]+=1
        except KeyError:
            words[word]= 1
pairs = words.itens()
pairs.sort(key=lambda x: x[1], reverse=True)

for p in pairs[:10]:
    print((p[0],p[1]))

