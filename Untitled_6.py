from tkinter import*
from random import*

n = 20
us_step = 0
pc_step = 0

def user():
    global n, us_step, pc_step
    us_step +=1 
    u = int(e.get())
    if (u in [1,2,3]) and (n-u)>0 :
        n = n - u
        t1.config(text = n*'| ')
        t2.config(text = str(n))
        t.config(text = 'Enter number 1 - 3')
    else:
        t.config(text = 'error')
    if n == 1:
        t2.config(text = 'user win', fg = 'red')

def pc():
    global n, us_step, pc_step
    pc_step +=1
    a = n // 4
    if n == (a+1):
        p = randint(1, 3)
        n = n - p
        t1.config(text = n*'| ')
    else:
        p = n - a
        t1.config(text = n*'| ')

        
    print (a   ) 
    t2.config(text = str(n))
    if n == 1:
        t2.config(text = 'pc win', fg = 'red')
        
w = Tk()
w.geometry('550x250')

t = Label(w, text = 'Enter number 1 - 3')
t.config(font = ('Arial', 15, 'bold'))
t.pack()

e = Entry(w, width = 20)
e.pack()

t1 = Label(w, text = n*'| ')
t1.config(font = ('Arial', 30, 'bold'))
t1.pack()


t2 = Label(w, text = str(n))
t2.config(font = ('Arial', 30, 'bold'))
t2.pack()

user_but = Button(w, text = 'user step', command = user)
user_but.config(font = ('Arial', 15, 'bold'), width = 30, bg = 'violet')
user_but.pack() 

pc_but = Button(w, text = 'pc step', command = pc)
pc_but.config(font = ('Arial', 15, 'bold'), width = 30, bg = 'green')
pc_but.pack() 


w.mainloop()
