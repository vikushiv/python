num=int(input())
numb=int()
lowerCase=int()
uperCase=int()
specialChar=int()
string=list()
while num>0:
     string.append(input())
     num-=1
for i in string:
    for j in i:
       # if j in i:
        if ord(j) in range(48,57+1):
            numb+=1
        elif ord(j) in range(97,122+1):
            lowerCase+=1
        elif ord(j) in range(65,90+1):
            uperCase+=1
        else:
            specialChar+=1
    if(numb==lowerCase & numb==uperCase & numb==specialChar):
        print("Equality for everyone")
    else:
        print("no Equality")

            

            