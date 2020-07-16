def factorial(n):
    if n>0:
        n=factorial(n-1)
        n=n*n
        return n

if __name__ == "__main__":
    num=int(input("Enter the number to know its factorial: "))
    fsct=factorial(num)
    print("the factorial is: ",fsct)