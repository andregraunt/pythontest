from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BcKpaJHXvzs&ab_channel=%D0%92%D0%A0%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%D0%B5'])
