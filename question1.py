a=int(input("Enter the Number :- "));
i=2
num=list()
while i<a:
    if a%i==0:
        num.append(i);
    i+=1
print(num)


