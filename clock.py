utf=int(input('Set time zone\nUTF'))
def getcurrent():
    global utf
    from time import time
    return int((time()%86400+3600*utf)/86400*100000)
a=getcurrent()

try:
    start=input('This clock is a weird clock.\nOn it,1day = 20h,1h=50min,1min=100sec.\nPress enter to start.')
except:
    pass
def printf():
    global a
    while getcurrent()==a:
        pass
    a=getcurrent()
    if a>100000:
        a=a%100000
    t='%.6d' % a
    if int(t[2:4])<50:
        print (int(t[0:2])*2,':',t[2:4],':',t[4:6])
    else:
        print (int(t[0:2])*2+1,':',int(t[2:4])-50,':',t[4:6])

sl=86400/100000
from time import sleep
while True:
    printf()
    
    sleep (sl-0.01)
    for tt in range(100):
        print ('')
    



    



