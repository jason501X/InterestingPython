a=int(input('enter an integer:')) 
x=[2]
y=3

def p(y):
    for d in x:
        if d**2 >= y:
            break
        
        if y%d==0:
            return False
    return True
    
while y**2<a:
    if p(y):
        x.append (y)
    y=y+1
    
toprint=[]
for b in x:
    count=0
    while a%b==0:
        a=int(a)
        count=count+1
        a=a/b
        
    if count > 1:
        toprint+=[str(int(b))+'^'+str(count)]
    if count == 1:
        toprint+=[str(int(b))]
if a!=1:
    toprint+=[str(int(a))]
print (' * '.join(toprint))
        


 
    
    

    





