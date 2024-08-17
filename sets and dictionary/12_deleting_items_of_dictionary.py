d={'name': 'suraj', 'age': 20, 'gender': 'male'}
#pop
d.pop('name')
print(d)

#popitem
d={'name': 'suraj', 'age': 20, 'gender': 'male'}
d.popitem()      #it deletes the last key value pair
print(d) 

#del
d={'name': 'suraj', 'age': 20, 'gender': 'male'}
del d['age']  #similar as pop
print(d) 

#clear
d.clear()  #it makes the dictionary empty
print(d)


#for 2d dictionaries
d2={'name':'Suraj Bhandari','course':'B.Tech','sem':4,'subjects':{'dsa':95,'maths':90,'architecture':80}}
del d2['subjects']['architecture']
print(d2)