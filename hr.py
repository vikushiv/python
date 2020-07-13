

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d=dict()
    count=int()
    for i in ar:
        d[i]=d.get(i,0)+1
    for i in d:
        count=count+int(d[i]/2)
    return count
        
if __name__ == '__main__':
   

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))

    
