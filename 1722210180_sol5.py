input_string=str(input());
input_list=input_string.split(' ')
output_string=str()
temp2=str()
temp=list()
for i in range(0,len(input_list)):
     temp=list(input_list[i]);
     temp.reverse();
     output_string=output_string+(temp2.join(temp))+' '

print(output_string,end="")

