#modulus function
a=abs(4)
print(a)
a=abs(-4)
print(a)

#power function
power=pow(2,3) # 2 to the power 3
print(power)

#max.min fucntion
maximum=max([1,2,3,4,5])
print('maximum is',maximum)
minimum=min([1,2,3,4,5])
print('minimum is',minimum)

#roundoff function
pie=22/7
print(pie)
print(round(pie,2))  #only prints 2 decimal places


#integer division and modulus function
a=divmod(13,2)
print(a)

#binary_octal_and_hexadecimal
a=bin(99)
b=oct(99)
c=hex(99)
print(a,"\n",b, "\n",c)

#memory address function
suraj=20
print(id(suraj)) #same as the pointer storing the address of variables

#to get asci values of certain characters
print(ord('A'))

#len function......> this is used to find the length(how many elements present) in any string,list,tupple,dictionary
print("The length of the list is",len([2,3,5,6]))
print("The length of my name is",len("suraj"))


#sum function
any_list=[1,2,3,4,5]
print('The sum of the list is',sum(any_list))

#help function
#this will show the use guide of the above mentioned functions or whatever function

print(help(sum))
print(help('modules'))