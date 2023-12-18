import time

def oki():
    time.sleep(1)

a=0
while a<=700:
    print(a)
    a+=10
    oki()
else:
    print("Ok!")
