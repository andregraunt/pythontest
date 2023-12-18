# age1 = 20
# age2 = 30
# age3 = 40
#
# location1 = "london"
# location2 = "stambul"
# location3 = "amsterdam"
#
# tel1 = 52352
# tel2 = 52364
# tel3 = 52388
#
# client1 = "vasa"
# client2 = "feda"
# client3 = "petuh"
#
# print(client1 + ' jivet v ' + location1 + ', ego telefon nomer - ' +
#       str(tel1) + ', i emu = ' + str(age1) + ' let')
#
# print(client2 + ' jivet v ' + location2 + ', ego telefon nomer - ' +
#       str(tel2) + ', i emu = ' + str(age2) + ' let')
#
# print(client3 + ' jivet v ' + location3 + ', ego telefon nomer - ' +
#       str(tel3) + ', i emu = ' + str(age3) + ' let')

a = '9182'
print(a[0])
print(a[:2])
print(a[0:3])
print(a[2:])


# he

# def plus(h):
#     if h == 1:
#         return 1
#     else:
#         return h + plus(h - 1)
#
#
# print(sum(4))


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(3))
