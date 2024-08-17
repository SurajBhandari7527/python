
str=input("Enter the string")
L1=[]
for i in range(len(str)):
    if(str[i]==' '):
        L1.append(i+1)
for i in range(len(str)):
    if i in L1:
        print(chr(ord(str[i])-32),end='')
    else:
     print(str[i],end='')

