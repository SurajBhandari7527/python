'''string functions: Common functions(which works in all data types[sets,tupple,dictionary...])
                     String functions(which works only for string)'''
str="suRaj bhanDari "  #strings are immutable. all of these functions create a new string without affecting the original one
#common functions
print(len(str))
print(max(str))
print(min(str))
print(sorted(str),'sorted list')
print(sorted(str,reverse=True ), 'sorting in descending order')

#string functions
print(str.capitalize(),':capitalized string') #capitalizes the first letter of the string
print(str.title(),':titled string') #it capitalizes the first letter and the letter after space too
print(str.upper(),':upper')    # a new string with uppercases is generated without affecting the original one
print(str.lower(),':lower')
print(str.swapcase(),':swapcase')   #converts capital letter into small and small into capital
print(str.replace ('a','s'),':replace a with s')
print(str.find('j'),':find the position of j')
print(str.find("bhanDari"),':find the powition of bhanDari')
print(str.find(" "),':find the position of space')
#print(str.index('x')) #this will throw error when the character is not present in the string but
print(str.find('x')) # this will return -1 when the character is not present that's the only diff betn index and find
print(str.count('a'),':count') #counts how many times a appears in string
print(str.startswith('su'),': startswith "su"') #returns true or false
print(str.endswith('ng'),': endswith "ng"') 
print(str[0:5],"\n")  #0 to 4  # it is called slicing of string because string can be cut from any point using this 
print(str[0:-3])  # -3= total(15)-3 ---> 0:12
print(str[2:10:3]) #last one 3 means the increment of 3. just remember the form a,b,x but here x means increment
print(str[::-1])# it prints the reverse of the string  

name='suraj'
age=20
print('Hi {}, How are you? You are {} years old'.format(name,age),':format')
#positioning can be done as well                   
#                                                          0    1
print('Hi {1}, How are you? You are {0} years old'.format(age,name),':format with positioning')

print(str.isalpha(),':isalpha')    #it checks if all the characters in the strings are all alphabets
print('1234'.isdigit(),':is digit') #checks if all the characters in the strings are all digits(numeric)
print('suraj1234'.isalnum(),':isalnum') #checks if the string is made with alphabets and numbers only
print('suraj_bhandari1'.isidentifier(),':isidentifier')  #checks valid identifier or if special character is present "_" is allowed 

print('Hi my name is suraj'.split(),': split') #it splits the string and converts to the list of strings
print('Hi my name is suraj'.split('i'),': split over "i"') #splitting over a particular character of the string
print(''.join(['Hi', 'my', 'name', 'is', 'suraj']),':join simply') #just joins the words of the list
print(' '.join(['Hi', 'my', 'name', 'is', 'suraj']),':join with space') #joins the words of the list with space in between
print('-'.join(['Hi', 'my', 'name', 'is', 'suraj']),':join join with hyphen') #joins the words of the list with the hyphen in between

print('suraj          '.strip())      #removes the unnecessary spaces
                                                                                                                                                        