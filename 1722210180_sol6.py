def target_index(li,target):
    target_=list()
    for i in li:
        for j in li:
            if(li[i]+li[j]==target):
                target_[i].append(i);
                target_[i].append(j);

    
    return(tar);





target_index(list(input("Enter the list ")),int(input("Enter the number ")));