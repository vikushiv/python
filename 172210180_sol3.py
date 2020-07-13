import random;
randomNumber=random.randint(1,9);
counter=1;
prompt='Y'
while(prompt=='Y'):
    num=int(input("Enter the number to guess the number "));
    if num>randomNumber:
          print("Number is greater than system generated numnber ");
    elif num<randomNumber:
        print("Number is less then the system generated number ");
    else:
        print("Congratulations you got the number in",counter,"count");        
        prompt=str(input("Do you want to continue Y/N"));
        if (prompt=='Y'):
            randomNumber=random.randint(1,9);
            counter=0;
        else:
            prompt='N'
    counter+=1;
    

# print(randomNumber)