import math as mt
def fact(num):
    fact=1
    for n in range(1,num+1):
        fact=fact*n
    return fact


print(fact(26))
print(mt.pow(2,168))