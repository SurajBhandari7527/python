#1. empty set
s={} #it is wrong way
print( type(s)) #its dictionary because set and dictionary both have the same syntax
#to create empty set
s1=set({})  #typecasting
print(type(s1))

#1D and 2D sets
s2={1,2,3}
# s3={1,2,{3,4}}     this is not possible to create. this will throw error

# homo and hetero sets
s3={5,4,3,2,1}  #the order of elements in output is assigned acc to hash number called hashing.we don't have control of the position
s4={1,2,True,5.6,'suraj',2.2} # true means 1 so, both 1 and true cannot get printed because no duplicates allowed in sets
print(s3)
print(s4)


#type conversion to create set
 
s5=set([1,2,3])  #create set from list by type conversion
print(s5)


#2d set using frozenset
'''Question: Why can't you include a set inside another set in Python?

Answer:

In Python, sets are collections of unique, non hashable elements. The reason you can't include 
a set inside another set is because sets themselves are mutable. 
Since mutable objects can change, they can't have a fixed hash value, which is required for an object to be hashable.

Understanding the Problem
Hash Table Basics:

Hash Table: Both sets and dictionaries in Python are implemented using hash tables. A hash table uses hash values to quickly locate data. When you insert an item, its hash value determines where it is placed in the hash table. When you look up an item, the hash value is used to find its location.
Mutable vs. Immutable Objects:

Immutable Objects: Objects like integers, strings, and tuples are immutable. Once their hash value is computed, it remains constant. This makes them reliable for use in sets and as dictionary keys.
Mutable Objects: Objects like lists and regular sets can change their contents. If these objects were allowed in sets or as dictionary keys, their hash value could change if their contents are modified. This could disrupt the integrity of the hash table.
Why Updating Hash Values Isn't Practical
Hash Table Integrity:

Fixed Hash Locations: When an item is added to a set or a dictionary, its hash value determines its location in the hash table. If the hash value changes after insertion (because the object's contents change), the item might be placed in the wrong location or become inaccessible.
Rehashing Complexity: If the hash value of an item changes, the hash table would need to find and update the item's new location. This rehashing process is complex and inefficient, and it could lead to inconsistencies or errors in data retrieval.



Sets in Python use hash tables to manage and locate their elements efficiently. Each element in a set is associated with a hash value, 
which allows for quick lookups, additions, and deletions. However, Python sets themselves are mutable, which means their contents can change.
For an object to be used as an element in a set, it must be hashable, meaning its hash value must remain constant throughout its lifetime. 
This is why Python does not allow mutable data types, like regular sets, to be elements of other sets or keys in dictionaries.
If mutable types were allowed, modifying an element could change its hash value, leading to inconsistencies in the hash table and errors
 in data retrieval. To address this, Python provides frozenset, an immutable version of a set that is hashable and can be used as an element
 in other sets or as a dictionary key'''

#frozenset are immutable and hashable so we can use them to create 2d sets
fs1=frozenset([1,2,3,frozenset([4,5,6])])
print(fs1)

#set comprehension
print({i for i in range(1,11)})