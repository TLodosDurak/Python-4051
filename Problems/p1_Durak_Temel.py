"""
Python 4045
HW 2 Problem 1
Author: Temel Lodos Durak
Date: 02/05/23

"""
def line_number(file1: str, file2: str):
    '''
    line_number takes as parameters two strings representing file names.
    The function reads the file indicated by the first parameter and writes its
    lines prefixed by the line number to the file represented by the second parameter.
    '''
    
    try:
        input_file = open(file1, "r") 
    except FileNotFoundError as e:
        raise e
        
    output_file = open(file2, "w")
    
    
#Input file will be this file itself
file1_str = "p1_Durak_Temel.py"
file2_str = "p1_Durak_Temel.py.txt" #Output file will be created with this name
line_number(file1_str, file2_str)