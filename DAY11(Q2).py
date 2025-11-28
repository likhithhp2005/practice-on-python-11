n=input("enter the number: ")
n1=input("enter the 1st number to replace:")
n2=input("enter the 2nd numvber to replace:")
num_list=list(n)
print("num list",num_list)
for i in range(len(num_list)):
    if num_list[i]==n1:
        num_list[i]=n2
    elif num_list[i]==n2:
        num_list[i]=n1
print("replaced number list:",num_list)
n="".join(num_list)
print(n)