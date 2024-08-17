#  set operations: 
'''
1. union
2. intersection, difference
3. symmetric difference
4. membership test
5. iteration'''

# Union
s1={1,2,3}
s2={1,3,4,5,6}
print(s1 | s2)

# intersection
print(s1 & s2)

# difference
print( s1 -s2) # print those items of s1 which are not present in s2
print(s2 -s1) # print those items of s2 which are not present in s1

#symmetric diff( it is the items which are other than intersection of union of s1 and s2: (AUB)-(AnB) or (A-B)U(B-A))
print( s1 ^ s2)

# membership test
print( 1 in s1)
print( 3 not in s2)

# iteration
for i in s1:
    print(i)