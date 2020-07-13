strNum=int(input())
j=1
string=list()
string1=list()

while strNum>0:
    string.append(input())
    strNum-=1      


for i in string:
    vowel=int()
    cons=int()
    for j in i:
        if j in ['a','e','i','o','u']:
           vowel+=1
        else:
           cons+=1
    print(vowel,end=' ')
    print(cons,end=' ')
    print(vowel*cons)