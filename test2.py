exec('''import time\n\ndef lcg(s):\n    a,c,m=1664525,1013904223,2**32\n    while 1:s=(a*s+c)%m;yield s%101\n\ndef gn():return int(time.time()*1000)%100\n\nr=lcg(gn())\n\ndef gnum(n):\n    global r\n    return [next(r) if i%10 or i==0 else (r:=lcg(gn()),next(r))[1] for i in range(n)]\n\ndef tnum(n):\n    return [x+10 if i%15==0 else max(0,x-5) if i%20==0 else x for i,x in enumerate(n)]\n\n\nprint(tnum(gnum(10))[3])\n''')