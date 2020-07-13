numberOffstep=int(input())
steps=str(input())
count=int()
num=int()

for i in steps:
    if i=="D":
        
        if(count==0):
            num+=1
        count-=1
    else:
        count+=1
    
print(num)