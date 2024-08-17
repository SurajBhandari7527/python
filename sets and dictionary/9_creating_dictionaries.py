#empty dictionary
d1={}
print(d1)

#1d dictionary
d1={'name':'Suraj Bhandari','course':'B.Tech','sem':4}

#2d dictionary
d2={'name':'Suraj Bhandari','course':'B.Tech','sem':4,'subjects':{'dsa':95,'maths':90,'architecture':80}}
print(d2,'\n')

#typecasting
d3=dict([(1,3),('name','suraj'),('age',20)])
print(d3)

#duplicate keys not allowed
d1={'name':'suraj','name':'sahil'}
print(d1) # same keys cannot be used two times. Only the later one is considered 

# keys cannot be mutable
# d2={'name':'suraj',[1,2]:3}    this will throw error because [1,2] is a list and mutable instead we can do
d2={'name':'suraj',(1,2):3}  
print(d2) #as tuple is immutable