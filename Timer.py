def check(t):
    
    if len(t)>4:
        raise TypeError('More than 4 intems(dd,hh,mm,ss')
    while len(t)<4:
        t=[0]+t[:]
    return t
    
        

def ten(k):
    a=k//86400
    k=k%86400
    b=k//3600
    k=k%3600
    c=k//60
    k=k%60
    d=k
    return a,b,c,d

def sixty(k):
    return k[0]*86400+k[1]*3600+k[2]*60+k[3]

def wait(t):
    import time
    a=time.time()
    while True:
        y=time.time()
        if y-a>=t:
            break

def wait(t):
    from time import sleep
    sleep(t)
        
def timer():
    t=input('Time(dd:hh:mm:ss):\n').split(':')
    for a in range(len(t)):
        t[a]=int(t[a])
    t=check(t)
    m=input('Footstep long(dd,hh,mm,ss):\n').split(':')
    for a in range(len(m)):
        m[a]=int(m[a])
    m=check(m)
    print (t[0],'days',t[1],':',t[2],':',t[3])
    while True:
        wait(sixty(m))
        t=ten(sixty(t)-sixty(m))
        print (t[0],'days',t[1],':',t[2],':',t[3])
        if t <= (0,0,0,0):
            print ('TingLingLing!')
            break
        


p=''
while True:
    try:
        p=input('Press enter to start!')
    except:
        pass
    
    
    timer()
    
    
    
            


