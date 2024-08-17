str=input("Enter any string: ")
c=input("Enter which character's frequency to find: ")
count=0
for i in str:
    if(i==c):
        count=count+1
print("The frequency of",c,"is",count)