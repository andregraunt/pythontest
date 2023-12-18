l = [1, 2, 2, 3, 3, 4, 1]
m = set(l)
print(m)
lst = [15,50,60,97,78]
for x in lst:
    x = x + 1
    print(x)
num = 0
for i in range(5):
    num=num + 1
    print('Я ' + str(num) + ' кружка пива')
mas = ['Ленин', 'Сталин', 'Хрущёв', 'Брежнев', 'Горбачёв', 'Ельцин', 'Путин', 'Медведев']
# Ах да, Путин же потом вернулся. Нужно добавить его еще раз.
mas.append('снова Путин')
for x in mas:
    print('Был ' + x + ' а после него... ')
    
a = 0
b=0
while a < 10:
    a = a + 1
    if(b% 3)== 0 or (b%5) == 0:
        b=b+b
    print(a)  

#while b<10:
  #  b = b + 1
  #  if(b % 5) == 0:
      #  b=b+b
       # print(b)
#print(a+b)
