a = ['f','d','s','a']
x = -1 
scope = vars() 
for i in a: 
    scope['x']+=1 
print (a[x])
