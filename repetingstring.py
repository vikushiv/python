string=str(input())
num=int(input())
count=0
i=0  
c2=num%len(string)
for i in range(0,len(string)):
    if string[i]=="a":
        count+=1
count*=int(num/len(string))
for i in range(0,c2):
    if string[i]=="a":
        count+=1
        
print(count)