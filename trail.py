m=int(input())
n=input("")
lst=n.rstrip().split()
x=0
c=0
while(x<m):
    if(x<m-2 and lst[x]==lst[x+1] and lst[x]==lst[x+2]):
            x=x+2
            c=c+1
    else:
        x=x+2
        c=c+1
print(c)