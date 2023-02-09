"""
Python 4045
HW 2 Problem 3
Author: Temel Lodos Durak
Date: 02/05/23

"""
contact_list = []
def sort_contact(lst:list):
    """
    sort_contact takes in a contact list and sorts the list of tuples 
    by alphabetically looking at the first letter of the name field.
    """
    for i,tup1 in enumerate(lst): #Selection sort using double for loop
        min_tup_index = i
        for j,tup2 in enumerate(lst[i+1:], i+1):#nested forloop that starts from the next index
            if(lst[min_tup_index][0][0]>tup2[0][0]):     #comparing first letter of the function name of the min index with the current one
                min_tup_index = j
        temp = lst[i]                    #swapping their places
        lst[i] = lst[min_tup_index]
        lst[min_tup_index]= temp
    return lst   

#a
def add_contact(info: tuple):
    print("x")
    for i, contact in enumerate(contact_list):
        if(info[0] == contact[0]):
            contact_list[i] = info
            return False
    contact_list.append(info)
    sort_contact(contact_list)
    return True
