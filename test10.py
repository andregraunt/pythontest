
from math import*


sum = 0
for n in range(1, 65):
    m = int (pow(2, n - 1))
print("%2d: %d" % (n, m))
sum = sum + m


print ("sum = %d" % sum)
print ( 2**63 + 1)
print(9223372036854775808+9223372036854775808)

print(2**0)
print(1**0)
