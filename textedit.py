def write(a):
    print ('|'+files[a])
    global f
    f=0
    def prt(a):
       global f
       print (a[:f]+'|'+a[f:])
    def cor():
        global f
        if f<0:
            f=0
        elif f>len(files[a]):
            f=len(files[a])
    
    while True:
        h=tuple(input('editing '+a+':'))
        if h[0]=='move':
            f=f+h[1]
            cor()
            prt(files[a])
        elif h[0]=='MOVE':
            f=f+h[1]*3
            cor()
            prt(files[a]) 
        elif h[0]=='del':
            files[a]=files[a][:f-h[1]]+files[a][f:]
            f=f-h[1]
            cor()
            prt(files[a])
        elif h[0]=='ins':
            files[a]=files[a][:f]+h[1]+files[a][f:]
            f=f+len(h[1])
            cor()
            prt(files[a])
        elif h[0]=='exit':
            break



def newfile(a):
    global files
    files[a]=''



def delfile(a):
    global files
    del files[a]

def copyfile(a,b):
    global files
    files[b]=files[a]

def rename(a,b):
    global files
    copyfile(a,b)
    delfile(a)


def wait(a):
    from time import sleep
    sleep(a)


        
fil={}


try:
    files=open('.fi.txt','r')
except:
    files=open('.fi.txt','w')
    files.close()
    files=open('.fi.txt','r')
l=len(files.read())
files.close()
if l>0:
    files=open('.fi.txt','r')
    filet=files.read()
    files.close()
    filet=filet.split('||.||')
    if len(filet)%2==1:
        del filet[-1]
    for a in range(len(filet)):
        if a%2==0:
            fil[filet[a]]=filet[a+1]



files=fil

files['manual']='All commands:\n\tnewfile,a\n\tread,a\n\tcopy,a,b\n\tdel,a\n\tquit,\n\tls,\n\twrite,a:\n\t\tins,str\n\t\tdel,int\n\t\tmove,int\n\t\texit,'

while True:
    try:
        m=input('>>> ').split(',')
        if m[0]=='quit':
            break
        elif m[0]=='newfile':
            files[m[1]]=''
            
        elif m[0]=='write':
            write(m[1])
        elif m[0]=='read':
            print (files[m[1]])
        elif m[0]=='del':
            delfile(m[1])
        elif m[0]=='copy':
            copyfile(m[1],m[2])
        elif m[0]=='rename':
            rename(m[1],m[2])
        elif isinstance(m[0],int) and isinstance(m[1],int):
            for a in range(m[0]):
                print ('')
            wait(m[1])
        elif m[0]=='ls':
            for a in files:
                if a!='manual':
                    print (a)
        elif m[0]=='manual':
            print (files['manual'])
    except KeyboardInterrupt:
        print ('')
        break
    except:
        print ('File or Command wrong.')




















        


files=fil


fil=open('.fi.txt','w')

fi=''
co=''
for a in files:
    if a!='manual':
        fi=fi+a+'||.||'+files[a]+'||.||'

fil.write(fi)


