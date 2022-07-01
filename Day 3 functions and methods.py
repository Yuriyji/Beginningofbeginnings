from ast import Str
from tokenize import String


sentence = 'The very big house'    
print(sentence)
print(len(sentence))#len counts the number of characters in a string 
#useful for userinput to enforce a total number of characters.
print(sentence.upper()) #.upper is a method while print is a function
print('Thats a good password.')
print(sentence.find('house')) #find and replace method
print(sentence.replace('very', 'extremely'))
print(sentence.replace('house','mouse')) 
print('house' in sentence) #find produces an index 
                           #while (in) produces 
#len() is a function
#.upper() .lower() .title() .find() are functions
print('press enter to exit')
input()
