#Same difference as betn tuple and list frozenset is just like tuple while set is like list
# that means frozenset is immutable and can't be added anything or removed anything
fs=frozenset([1,2,3])
print(fs)
 
#All the write functions like |union &intersection -difference ^symmetric diff will work
#because they don't create any change in the original string
fs1=frozenset([1,2,3])
fs2=frozenset([3,4,5,6])
print(fs1|fs2)
print(fs1&fs2)
print(fs1-fs2)
print(fs1^fs2)

# frozensets are basically the immutable version of sets. we can use its property like unordered, no duplicates and again covert to list
fss=frozenset([1,2,2,2,3])
print(fss)
l=list(fss)
print(l)