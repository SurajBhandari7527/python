#[expression for iteration if condition]
#list=[ expression for item in iterable ]
a=[1,2,3,4,5]
b=-3
#output=[-3,-6,-9,-12,-15] using list comprehension

a=[i*b for i in a]
print(a)

#qn# nested if with list comprehension
basket=['apple','banana','cherry','guava']
my_fruits=['apple','kiwi','grapes','banana']
#add a new list from my_fruits if the fruit exists in the basket and also starts with 'a'

new_list=[fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')] 
print(new_list)

