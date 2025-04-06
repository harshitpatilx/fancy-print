import time
import random

def prinj(string):
    bk = ''
    for i in string:
        while True:
            time.sleep(0.03)
            r = random.randint(32, 125)
            rn = chr(r)
            print(bk, rn, sep='')
            if rn == i:
                bk+=rn
                break

a = input("Enter ")
prinj(a)
time.sleep(5)
