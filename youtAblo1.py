from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
from turtle import *
a = textinput("Link", ' ')
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
      ydl.download([f'{a}'])
 
