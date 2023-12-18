i = 100
j = 200
while i < 105:
    while j < 205:
        if j == 203:
            break
        print('J', j)
        j += 1
    print('I', i)
    i += 1
