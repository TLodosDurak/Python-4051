"""
Python 4045
HW 2 Problem 2
Author: Temel Lodos Durak
Date: 02/05/23

"""
#a
import math


result_list1 =[ (a,b,c) for a in range(1,101) for b in range(1,101) for c in range(1,101) if math.pow(a,2)+math.pow(b,2)==math.pow(c,2)]
print(result_list1)

#b
str_list1 = ['one','seven','three', 'two', 'ten']
result_list2 = [(len(word), word.upper()) for word in str_list1 if(len(word)>3)]
print(result_list2)

#c
str_list2 = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
result_list3 = [x[1]+", "+ x[0] for x in [full.split() for full in str_list2]]
print(result_list3)

#d
def concatenate(separator: str, *args:str):
    return separator.join(args)
        
print(concatenate(':', "one", "two", "three"))
    
