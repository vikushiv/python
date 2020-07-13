t=int(input())
n=int(input())
stringoutput=list()
str1 = list(input().split())
str2=''
while t>0:
    for i in range(0,len(str1)):
        stringoutput.append(str1[i][0])
    t-=1   
    
for i in stringoutput:
    str2+=i
print(str2)
m=1
for i in stringoutput:
    freq=stringoutput.count(i)
    if freq==m:
        j=i
print("I am alone ",end=j)