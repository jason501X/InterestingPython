from random import randint
c=0
import time
f=time.time()
def ran():
    global c
    d=time.time()
    while abs(d-int(d))>0.0001:
        d=d*10
    return (d%100+c*d)%100
c=c+ran()
def sq(a,b,c,d,t):
    ret=[]
    while len(ret)<t:
        ret.append(a*len(ret)**3+b*len(ret)**2+c*len(ret)+d)
    return ret,a*len(ret)**3+b*len(ret)**2+c*len(ret)+d


    
def ssq(a,b,c,d,r,t):
    m=sq(a,b,c,d,t)[0]
    ret=[r]
    while len(ret)<t:
        ret.append(ret[-1]+m[len(ret)-1])
    return ret,ret[-1]+m[len(ret)-1]    

timer=0
def timer_start():
    global timer
    timer=time.time()
def timer_stop():
    global stop
    stop=time.time()
def timer_read():
    global timer
    global stop
    return stop-timer
mark=0
def que(t,a,c):
    global mark
    timer_start()
    print ('What\'s the next number? Answer in '+str(t)+' seconds.')
    ans=input(str(a[0])+'\nAnswer: ')
    timer_stop()

    if timer_read()<t:
        if ans==a[1]:
            mark+=c[0]
        else:
            mark+=c[1]
    else:
        if ans==a[1]:
            mark+=c[2]
        else:
            mark+=c[3]
    
def test():
    try:
        e=input('This quiz has 10 questions.\nReady?Press enter.')
    except:
        pass
    global mark
    mark=0
    que(20,sq(0,0,randint(1,10),randint(1,50),5),[5,0,2.5,0])
    que(20,sq(0,0,randint(1,20),randint(1,50),5),[5,0,2.5,0])
    que(40,sq(0,randint(1,2),randint(1,5),randint(1,30),6),[7.5,0,3.75,0])
    que(40,sq(0,randint(1,5),randint(1,10),randint(1,30),6),[7.5,0,3.75,0])
    que(60,sq(randint(1,2),randint(1,2),randint(1,5),randint(1,20),8),[10,0,5,0])
    que(60,sq(randint(1,5),randint(1,5),randint(1,5),randint(1,20),8),[10,0,5,0])
    que(60,sq(randint(1,5),randint(1,10),randint(1,5),randint(1,20),8),[10,0,5,0])
    que(90,ssq(0,randint(1,2),randint(1,5),randint(1,20),randint(1,50),9),[15,0,5,0])
    que(90,ssq(randint(1,2),randint(1,5),randint(1,10),randint(1,20),randint(1,50),9),[15,0,5,0])
    que(90,ssq(randint(1,5),randint(1,10),randint(1,10),randint(1,20),randint(1,50),9),[15,0,5,0])
    print (('Your score is'),int(mark))
    a=mark//20
    if a==0:
        print ('Try again!')
    if a==1:
        print ('You can do better!')
    if a==2:
        print ('Good!')
    if a==3:
        print ('Well-done!')
    if a>=4:
        print ('Outstanding!')
    
test()
