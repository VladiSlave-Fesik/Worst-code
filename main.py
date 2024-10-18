import time

def lcg(s):
    a,c,m=1664525,1013904223,2**32
    while 1:s=(a*s+c)%m;yield s%101

def gn():return int(time.time()*1000)%100

r=lcg(gn())

def gnum(n):
    global r
    return [next(r) if i%10 or i==0 else (r:=lcg(gn()),next(r))[1] for i in range(n)]

def tnum(n):
    return [x+10 if i%15==0 else max(0,x-5) if i%20==0 else x for i,x in enumerate(n)]


print(tnum(gnum(10))[3])
