def toh(n,from_bar,to_bar,aux_bar):
    if n==1:
        print("move disk 1 from bar ",from_bar," to bar ",to_bar)
        return
    toh(n-1,from_bar,aux_bar,to_bar)
    print("move disk",n,"form bar ",from_bar," to bar ",to_bar )
    toh(n-1,aux_bar,to_bar,from_bar)

n=4
toh(n,'A','C','B')