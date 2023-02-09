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
def sort_funs_tuples(fun_tuple: tuple):
    '''
    Takes in a tuple of tuples and returns a sorted tuple of tuples according to 
    alphabetic order of the first letter of the first element of each tuple that corresponds to function name
    '''
    result = list(fun_tuple)
    for i,tup1 in enumerate(result): #Selection sort using double for loop
        min_tup_index = i
        for j,tup2 in enumerate(result[i+1:], i+1):#nested forloop that starts from the next index
            if(result[min_tup_index][0][0]>tup2[0][0]):     #comparing first letter of the function name of the min index with the current one
                min_tup_index = j
        temp = result[i]                    #swapping their places
        result[i] = result[min_tup_index]
        result[min_tup_index]= temp
    return tuple(result)    

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
    file_all = input_file.readlines()
    result = []         #Creating lists for the tuple of tuples we are going to return
    current = []        #and a list for each individual tuple
    for i, line_str1 in enumerate(file_all):
        body = ""
        if("def" in line_str1):
            fun_name = line_str1[4:line_str1.find('(')]#from first letter of function name to (
            current.append(fun_name)
            current.append(i+1) #line number is i+1 since i starts from 0
            for j, line_str2 in enumerate(file_all[i:]): #starting from the functions index
                if (j == 0 or line_str2.startswith((' ', '\t'))): #body will stop once line does not start with empty space or isnt the def line which is j ==0
                    for char in line_str2:
                        if(char != '#'):
                            body = body + char
                        else:
                            break
                else:
                    break  
            current.append(body)
            result.append(tuple(current))
        current = []
    input_file.close()
    return sort_funs_tuples(tuple(result))

print(parse_functions("funs.py"))
            

    
