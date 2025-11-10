Lab Overview: Learning how to use git and lambda in writing python code.

Project structure:
OOP-LAB1              
├── Cities.csv                      
├── data_processing.py	  
├── README.md   

Design Overview:
def filter(self, condition) 
Purpose: Filters rows based on user's condition and return a new Table of filtered data. If condition(row) returns True, the row will be added into the filtered_data set.

def aggregrate(self, func, column)
Purpose: Applies an aggregation function to specific column across all rows. Using for loop to go throw all the rows in the table, if column is in that row and it's not empty it will be added into the value set

