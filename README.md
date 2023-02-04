# Python-4045 <br>
**Python-4045 HW2 Problem Sets** <br>
**Author: Temel Lodos Durak** <br>
**Date: 02/04/2023** <br>
**Github Account: TLodosDurak** <br>
**Repo URL:** https://github.com/TLodosDurak/Python4045-HW2.git 

---
# Problem 1
Write the code for this problem in a file named p1_Lastname_Firstname.py, as required above.
In this problem we parse Python files. (This is typically done by IDE applications, like Spyder or
PyCharm, that must understand the structure of code to do syntax highlighting, for instance.)
<br><br>
a) Write a function called line_number that takes as parameters two strings representing file names.
Assume these are text files. The function reads the file indicated by the first parameter and writes its
lines prefixed by the line number to the file represented by the second parameter.
The function must have a proper docstring and annotations. Use try/except and in case of an error print
a user-friendly message to the terminal and re-raise the exception.
Example: suppose file test.py has this content:<br>
```
import math
y = math.sqrt(2)
print(y)
```
Function call line_number(‘test.py’, ‘test.py.txt’) creates a new file named test.py.txt with content:
```
1. import math
2. y = math.sqrt(2)
3. print(y)
```
Write a main function that tests function line_number on the problem 1 Python source file itself. Make
sure you don’t overwrite your program by mistake.<br><br>
b) Write a function called parse_functions that takes as parameter a string representing the name of
a .py file. The function reads and parses the Python file and returns a tuple of tuples where each tuple
has its element 0 a function name, element 1 the line number, and element 2 the function code as a
string (signature and body), with all comments removed.
The top-level tuple returned must be ordered alphabetically by the function name.
Function parse_functions must have a proper docstring and annotations. Use try/except and in case of
an error print a user-friendly message to the terminal and re-raise the exception.
<br><br>
Write in the main function code that calls parse_functions on the problem 1 Python file and displays
the returned tuple.
<br><br>
Example: suppose file funs.py has this content:
```
# File with sample functions.
def sum(x, y): # sums up two numbers
    """ Adds two numbers.
    Returns the sum."""
    return x + y
# Returns the product.
def mul(x, y): # multiplies two numbers
    # z is a local variable
    z = x * y
    return z
def print_pretty(a):
    print("The result is {:.3f}.".format(a))
# test these functions:
print_pretty(mul(10, sum(3, 5)))
``` 
<br><br>
A call to parse_functions("funs.py") returns tuple:
( ("mul", 9, 'def mul(x, y):\n\tz = x * y\n\treturn z\n' ),
("print_pretty", 14, 'def print_pretty(a):\n\tprint("The result is {:.3f}.".format(a))\n' ),
("sum", 3, 'def sum(x, y):\n """ Adds two numbers. \n Returns the sum."""\n\yreturn a + b\n' ) )

# Problem 2.
Write the code for this problem in a file named p2_Lastname_Firstname.py, as required above.
<br><br>
a) Write a list comprehension that returns all tuples (a,b,c), with a,b,c integers, such that 1<=a,b,c<=100
and a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>.
<br><br>
b) Consider a list of strings, like this: ['one', 'seven', 'three', 'two', 'ten']. Write a list comprehension that
produces a list with tuples where the first element of the tuple is the length of an element in the initial
list, the second element of the tuple is the element of the initial list capitalized, and the resulting list
contains only tuples for strings with the length longer than three characters.
For our example the list comprehension should return [(5, 'SEVEN'), (5, 'THREE')].
<br><br>
c) Consider a list of full names (formatted “Firstname Lastname”), like["Jules Verne", "Alexandre
Dumas", "Maurice Druon"]. Write a list comprehension that produces a list with the full names in this
format: “Lastname, Firstname”. The resulting list should look like ['Verne, Jules', 'Dumas, Alexandre',
'Druon, Maurice'].
The simplest solution may involve a nested comprehension: [ .... for ... in [ ... for ... in ... ]].
<br><br>
d) Write a function called concatenate that takes as parameter a separator (a string) and an arbitrary
number of additional arguments, all strings, and that returns the concatenation of all given strings using
the given separator.
<br><br>
Example: concatenate(‘: ‘, “one”, “two”, “three”) returns “one: two: three”
and concatenate(‘ and ‘, “Bonny”, “Clyde”) returns “Bonny and Clyde”.
For a single string we have: concatenate(‘ and ‘, “single”) return “single”.

# Problem 3. 
Write the code for this problem in a file named p3_Lastname_Firstname.py, as required above.

For the following, all functions must have a proper docstring and annotations. Use try/except and in
case of an error print a user-friendly message to the terminal and raise or re-raise the exception.
<br><br>
For this problem we will develop a contact list, similar to what is on smartphones.
The contact list data structure is a list of tuples with the following format (name, nickname, phone#).
For instance, a sample contact list could be [("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B",
"Belcalis", "305-4399521"), ("Earl Simmons", "DMX", "305-1010101")].
The contact list must be stored in a Python list of tuples, as above, always sorted alphabetically on the
name field. An empty contact list is represented by the empty list []. For your solution to get any credit
do NOT use dictionaries.
<br><br>
a) Write a function that adds a contact to a contact list. If the contact name existed before in the list then
it will be changed to the new entry and the function returns False. Otherwise, the function should
return True.
<br><br>
b) Write a function that removes a contact from a contact list. If the contact name existed before in the
list then the function returns True. Otherwise, the function should return False.
<br><br>
c) Write a function that finds a contact tuple from a contact list by passing the contact name or contact
nickname. Use default parameter values to deal with this choice. The function returns the tuple if the
contact is found and returns None otherwise.
<br><br>
d) Write a function that saves a contact list to a .CSV file. The function takes as parameter the file
name. The CSV file format must have name, nickname, phone# on a line for each contact in the list.
<br><br>
e) Write a function that reads a contact list from a .CSV file with the format described for part d). The
function takes as parameter the file name and returns the contact list object (... sorted alphabetically).
<br><br>
f) Write a main function that tests all the functions above.
<br><br>
g) EXTRA CREDIT: 5 points
Write a function test where you use the testif function from Module 2 to test the functions written for
parts a)-e).

# Problem 4. 
Write the code for this problem in a file named  p3_Lastname_Firstname.py, as required above.
<br><br>
For this problem we work with CSV files and dictionaries using data from IMDB lists with top rated
and top grossing movies.<br><br>
These CSV files are linked on the Homework 2 Canvas page:
- imdb-top-rated.csv, listing the ranking of the top rated 250 movies. It has this format:
Rank,Title,Year,IMDB Rating
- imdb-top-grossing.csv, listing the ranking of the highest grossing 250 movies. It has this format:
Rank,Title,Year,USA Box Office
- imdb-top-casts.csv, listing the director and cast for the movies in the above files. It has this format:
Title,Year,Director,Actor 1,Actor 2,Actor 3,Actor 4,Actor 5. The actors are listed in billing order.
This file does not have a heading.<br>
These files are from Duke University and seem to date from 2014.

<br><br>
a) Write a function called display_top_collaborations that displays the ranking of tuples (director, first
billed actor (i.e. Actor1), and number of movies) for movies in which the director and actor worked
together also listed in the top rated movie list. The list should be in descending ordered of the total
number of movies that director and that actor worked together. For equal values the order does not
matter.
Notice that the number of movies in the imdb-top-casts.csv file exceeds the number of movies in imdb-
top-rated.csv. You may have to open the csv files like this: open(filename, 'r', encoding = 'utf-8').
<br><br>
b) Write a function called display_top_directors that displays the ranking of movie directors from the
top grossing list ordered by the total box office money they produced.
<br><br>
c) Write a main() function that tests the code from parts a) and b).
<br><br>
Take a screenshot of the program’s output (parts a, b, c) where each printed ranking list is limited to
the first 5 entries and insert it in the doc file right after the code. You get 8 points deducted if the
screenshot is missing.
