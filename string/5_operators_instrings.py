'''operators in string
  1. Arithmetic operator 
  2. Relational Operator
  3. logical
  4. loops on string
  5. membership operators'''
s='suraj'
print(s*5) #arithmetic
print('suraj'=='suraj') #relational
print('suraj'>'bhandari') #it is the lexiographical comparison that means like dictionary
print('suraj' >'Suraj') #comparison in asci value
print('hello' and 'world')
print("" and 'world') #if there is something written inside the string then it means true
#if the string is empty then it means false. it prints at the point when output is 100% sure
#in above it will print false string as soon as it finds one false between 'and' operators


print('hello' or 'world') # it will print the first string because it prints the T string at the point where output is 100%sure
# in case of 'or' operator when first one is true its true irrespective of the second string
print(not 'hello')
print(not "") #this will print true because empty string is false and not makes it true