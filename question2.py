n=int(input("Enter the number of element in list:- "))
a=list()
lst=list()
while n>0:
    a.append(int(input()));
    n-=1;

for i in range(0,len(a)):
    if a[i]<5:
        lst.append(a[i]);
print(lst,end=" ")