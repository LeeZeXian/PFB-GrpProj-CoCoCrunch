# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:16:39 2024

@author: Lee, Ze-Xian

"""


def check_expenses(data):
    text1, text2 = find_largest_number(data)

    return text1[0], text2

def find_largest_number(data):
    largest_number = float('-inf') 
    largest_name = []  

    for index, number in enumerate(data):
        if number[1] > largest_number:
          largest_number = number[1]
          largest_name = [number[0]] 
        elif number[1] == largest_number:
          largest_name.append(index) 
                
    return largest_name, largest_number


def overhead(data):
    
    # Check data for largest number
    output1, output2 = check_expenses(data)
    
    # Write into Summary.txt file
    with open('summaryreport.txt', 'a') as outfile:
        outfile.write("[Highest Overhead]: %s  : %s%%  \n" % (output1, output2))
            
    



