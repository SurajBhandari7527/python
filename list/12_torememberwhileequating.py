#if we want to copy the same elements of one list to another and want make change to one list but not to another then following 
#way wont work
L1= [1,2,3]
L2=L1
L1.append(4)
print(L1)
print(L2) #The changes will occur in both the list because list stores the addresses of the elements so changes done to the addresses
# of first list will create changes in the list of the second list elements too. both are the same actually.but we can use copy


L3=[1,2,3]
L4=L3.copy()
L3.append(4)
print(L3)
print(L4) 
'''this shallow copy will create a another storage address of the elements 
and stores it in the list. so no changes when first list is edited'''
