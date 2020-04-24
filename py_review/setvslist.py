from random import randint
import time

def addToSet(ntimes, maxnum):
    start = time.time()

    s = set()
    for n in range(ntimes):
        x = randint(0,maxnum)
        s.add(x)

    elapsed = time.time() - start

    print(s)
    print(elapsed)

def addToList(ntimes, maxnum):
    start = time.time()

    l = []
    for n in range(ntimes):
        x = randint(0,maxnum)
        if x not in l:
            l.append(x)

    elapsed = time.time() - start

    print(l)
    print(elapsed)

ntimes = 10000000
maxnum = 1000
addToSet(ntimes, maxnum)
addToList(ntimes, maxnum)
