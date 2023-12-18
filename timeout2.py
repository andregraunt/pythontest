from threading import*
from turtle import *
def hello():
    #os.system('')
    print("test end")
    #time()
#a = textinput('zman shel test in sec : ', ' ')

t = Timer(numinput('zman shel test in sec : ', ' '), hello)
t.start() 
#time
