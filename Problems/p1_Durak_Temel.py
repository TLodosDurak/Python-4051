"""
Python 4045
HW 2 Problem 1
Author: Temel Lodos Durak
Date: 02/05/23

"""
#a)
def line_number(file1: str, file2: str):
    """
    line_number takes as parameters two strings representing file names.
    The function reads the file indicated by the first parameter and writes its
    lines prefixed by the line number to the file represented by the second parameter.
    """
    
    try:
        input_file = open(file1, "r") 
    except FileNotFoundError as e:
        raise e
        
    output_file = open(file2, "w")
    
    new_str = '' 
    count = 1
    for line_str in input_file:
        new_str += "{:4}.".format(count) + line_str
        count+= 1
    output_file.write(new_str)
    input_file.close() #closing file streams
    output_file.close()
    
#Input file will be this file itself
file1_str = "p1_Durak_Temel.py"
file2_str = "p1_Durak_Temel.py.txt" #Output file will be created with this name
line_number(file1_str, file2_str)

#b)
def parse_functions(file_name: str):
    """
    parse_functions takes as parameter a string representing the name of
    a .py file. The function reads and parses the Python file and returns
    a tuple of tuples where each tuple has its element 0 a function name, 
    element 1 the line number, and element 2 the function code as a string
    (signature and body), with all comments removed. The top-level tuple
    returned is ordered alphabetically by the function name.
    """
    try:
        input_file = open(file_name, "r") 
    except FileNotFoundError as e:
        raise e
    count = 1
    result = []
    current = []
    body=""
    for line_str in input_file: 
        if("def" in line_str):
            fun_name = line_str[4:line_str.find('(')]#from first letter of function name to (
            current.append(fun_name)
            current.append(count)
            result.append(tuple(current))
        count+=1
        current = []
    return tuple(result)
print(parse_functions("funs.py"))
            
    
