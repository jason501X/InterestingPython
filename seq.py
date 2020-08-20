u='''Calaulating sequences using tong1'xiang4'gong1'shi4.'''
print (u)

def sl(a,b):
    x=(b-a)/2
    y=a-x
    return [x,y]

def solve(a,b,c):
    x=(c-2*b+a)/6
    y=(b-a-x*6)/2
    z=a-x-y
    return [x,y,z]

def equal(m):
    for a in m:
        if a!=m[0]:
            return False
    return True

def one(a):
    plus=[]
    minus=plus[:]
    times=minus[:]
    div=times[:]
    for n in range(len(a)-1):
        plus.append(a[n]+a[n+1])
        minus.append(a[n+1]-a[n])
        times.append(a[n]*a[n+1])
        try:
            div.append(a[n+1]/a[n])
        except:
            pass
    ret=[]

    if equal(plus):
        try:
            ret.append(plus[0]-a[-1])
        except:
            pass
    if equal(minus):
        try:
            ret.append(minus[0]+a[-1])
        except:
            pass
    if equal(times):
        try:
            ret.append(times[0]/a[-1])
        except:
            pass
    if equal(div):
        try:
            ret.append(div[0]*a[-1])    
        except:
            pass
    if ret==[]:
        return [None]
    else:
        return ret

def two(m):
    f=sl(m[1]-m[0],m[2]-m[1])
    f.append(m[0])
    for a in range(len(m)):
        if f[0]*a*a+f[1]*a+f[2]!=m[a]:
            return [None]
    return [f[0]*len(m)*len(m)+f[1]*len(m)+f[2]]

def three(a):
    f=solve(a[1]-a[0],a[2]-a[1],a[3]-a[2])
    f.append(a[0])
    for d in range(len(a)):
        if f[0]*d*d*d+f[1]*d*d+f[2]*d+f[3]!=a[d]:
            return [None]
    return [f[0]*len(a)**3+f[1]*len(a)**2+f[2]*len(a)+f[3]]


def abcd(a):
    ret=[]
    if one(a)[0]!=None:
        ret.append(one(a)[0])
    try:
        if two(a)[0]!=None:
            ret.append(two(a)[0])
    except:
        pass
    try:
        if three(a)[0]!=None:
            ret.append(three(a)[0])
    except:
        pass

    if len(ret)==0:
        ret=[None]
    
    return ret

def first(a):
    ret=[]
    for e in abcd(a):
        if e!=None:
            ret.append(e)
    plus=[]
    minus=plus[:]
    times=minus[:]
    div=times[:]
    for n in range(len(a)-1):
        plus.append(a[n]+a[n+1])
        minus.append(a[n+1]-a[n])
        times.append(a[n]*a[n+1])
        try:
            div.append(a[n+1]/a[n])
        except:
            pass
    for e in abcd(plus):
        if e!=None:
            ret.append(e-a[-1])
    for e in abcd(minus):
        if e!=None:
            ret.append(e+a[-1])
    for e in abcd(times):
        if e!=None:
            try:
                ret.append(e/a[-1])
            except:
                pass
    for e in abcd(div):
        if e!=None:
            ret.append(e*a[-1])
    tr=[]
    for a in ret:
        if not(a in tr):
            tr.append(a)
    return sorted(tr)

def second(a):
    ret=[]
    plus=[]
    minus=plus[:]
    times=minus[:]
    div=times[:]
    for n in range(len(a)-1):
        plus.append(a[n]+a[n+1])
        minus.append(a[n+1]-a[n])
        times.append(a[n]*a[n+1])
        try:
            div.append(a[n+1]/a[n])
        except:
            pass

    for e in first(a):
        if e!=None:
            ret.append(e)



    for e in first(plus):
        if e!=None:
            ret.append(e-a[-1])
    for e in first(minus):
        if e!=None:
            ret.append(e+a[-1])
    for e in first(times):
        if e!=None:
            try:
                ret.append(e/a[-1])
            except:
                pass
    for e in first(div):
        if e!=None:
            ret.append(e*a[-1])
    tr=[]
    for a in ret:
        if not(a in tr):
            tr.append(a)
    return sorted(tr)

def third(a):
    ret=[]
    for e in first(a):
        if e!=None:
            ret.append(e)


    ret=[]
    plus=[]
    minus=plus[:]
    times=minus[:]
    div=times[:]
    for n in range(len(a)-1):
        plus.append(a[n]+a[n+1])
        minus.append(a[n+1]-a[n])
        times.append(a[n]*a[n+1])
        try:
            div.append(a[n+1]/a[n])
        except:
            pass
    for e in second(plus):
        if e!=None:
            ret.append(e-a[-1])
    for e in second(minus):
        if e!=None:
            ret.append(e+a[-1])
    for e in second(times):
        if e!=None:
            try:
                ret.append(e/a[-1])
            except:
                pass
    for e in second(div):
        if e!=None:
            ret.append(e*a[-1])
    tr=[]
    for a in ret:
        if not(a in tr):
            tr.append(a)
    return sorted(tr)

def fourth(a):
    ret=[]
    for e in first(a):
        if e!=None:
            ret.append(e)


    ret=[]
    plus=[]
    minus=plus[:]
    times=minus[:]
    div=times[:]
    for n in range(len(a)-1):
        plus.append(a[n]+a[n+1])
        minus.append(a[n+1]-a[n])
        times.append(a[n]*a[n+1])
        try:
            div.append(a[n+1]/a[n])
        except:
            pass
    for e in third(plus):
        if e!=None:
            ret.append(e-a[-1])
    for e in third(minus):
        if e!=None:
            ret.append(e+a[-1])
    for e in third(times):
        if e!=None:
            try:
                ret.append(e/a[-1])
            except:
                pass
    for e in third(div):
        if e!=None:
            ret.append(e*a[-1])
    tr=[]
    for a in ret:
        if not(a in tr):
            tr.append(a)
    return sorted(tr)



    

while True:

    a=input('seq:').split(',')
    for t in range(len(a)):
        a[t]=int(a[t])
    print ('Answer is')
    try:
        print (fourth(a))
    except RuntimeError:
        try:
            print (third(a))
        except RuntimeError:
            try:
                print (second(a))
            except RuntimeError:
                print (first(a))
        
