# Complete the jumpingOnClouds function below.
n = int(input())
c = list(map(int, input().rstrip().split()))

count=0
i=0
while i<n-1:
    if i<n-2 and c[i+1]==0 and c[i+2]==0:
        count+=1
        i+=2
    elif i<n-1 and c[i+1]==1:
        i+=2
        count+=1
    else:
        i+=1
        count+=1
print(count)    



        

   
print(count)


    

    

    

    

    

    
