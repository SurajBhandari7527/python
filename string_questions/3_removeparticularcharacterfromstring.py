str=input("Enter the string: ")
ch=input("Enter the character to remove: ")
length=len(str)
for i in str:
    if(i==ch):
        continue
    else:
     print(i, end="")
print(str)