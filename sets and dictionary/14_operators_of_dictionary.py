#membership operator
# it works on the key of the dictionary not on the value
d2={'name':'Suraj Bhandari','course':'B.Tech','sem':4,'subjects':{'dsa':95,'maths':90,'architecture':80}}
print( 'Suraj Bhandari' in d2)
print('name' in d2)

#iteration
d2={'name':'Suraj Bhandari','course':'B.Tech','sem':4,'subjects':{'dsa':95,'maths':90,'architecture':80}}
for i in d2:
    print(i) # this only print the keys

# to print the values we can use extraction using keys
for i in d2:
    print(i,d2[i])