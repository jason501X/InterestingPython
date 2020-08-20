alphabet='abcdefghijklmnopqrstuvwxyz'
aph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
blphabet=[8167,1492,2782,4253,12702,2228,2015,6094,6966,153,772,4025,2406,6749,7507,1929,95,5987,6327,9056,2758,978,2360,150,1974,74]
bet={}
for a in range(len(alphabet)):
    bet[alphabet[a]]=blphabet[a]
while True:
    word=input('your text:\n')
    

    for e in range(len(word)):
        if (not word[e] in alphabet):
            if word[e] in aph:
                for a in range(len(alphabet)):
                    if aph[a]==word[e]:
                        word=word[:e]+alphabet[a]+word[e+1:]
            else:
                word=word[:e]+'|'+word[e+1:]
    word=''.join(word.split('|'))

    

    num=[]
    for n in word:
        num.append(bet[n])
    print ('score:',int(sum(num)//len(num)))
    print ('the score higher,the word commoner.')
