''' arrays and lists are similar but they are diff in folowing points
    1. array has fixed sized declared at the beginning while lists has dynamic size
    2. homogeneous-int array only stores intergers, char arr only stores character but list stores everything
    3. array has speed of execution faster than list
    4. memory is occupied more by lists than arrays'''

# list stores element's address. it can be compared to the pointer. for eg: *ptr=&a is same as list=[a]. that means that 
# numbers and string inside the list are stored in random storage locations and list stores the addresss of them. not like array to
# store the adjacent in same sequence of locations. further list is like dynamic array.

'''n Python, lists are referred to as "referential arrays" because they store references to objects rather than 
the objects themselves. This means that each element in a list is a reference (or pointer) to an object
 located elsewhere in memory.'''

x = [1, 2, 3]
y = x
y[0] = 10
print(x)  # Output: [10, 2, 3] 

'''Characterstics of a List
- Ordered (a=[1,2,3] and b=[3,2,1] are not equal. order matters)
- Changeble/Mutable
- Hetrogeneous
• Can have duplicate elements ( a=[1,2,1,1])
- are dynamic
-can be nested( a=[1,2,3,[3,2]])
-items/elements can be accessed or extracted
-can contain any kind of objects in python▸'''