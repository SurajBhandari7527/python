''' to print        *
                   ***
                  *****
                 *******    '''
a=input("enter the number of rows")
a=int(a)
for i in range(a):
        for j in range(a-i-1):
            print(" ",end="")           #end="" mustbe written to execute loops in the same line otherwise it will be printed in another line
        for k in range(2*i+1):       
            print("*",end="")
        print("\n")