# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
file_list = glob.glob('*.csv')


# Write the read_table and read_database functions below

def read_table(filename):
    '''(str) -> Table
    given a data return the table representation of the table
    REQ: File must be a comma-separated file.
    REQ: Column names must be unique
    '''
    # set a variable which represents a table
    table1 = Table()
    # open the file
    table = open(filename, 'r')
    # read the first line of code
    table_clean = table.readline()
    table_clean = table_clean.strip().split(",")
    # loop through the file
    for element in table_clean:
        # ma
        table_dict = {element: []}
        # use table_add_column to add column
        table1.table_add_column(table_dict)
    # loop through the lines
    for i in table:
        i = i.strip().split(",")
        # add the content from the line with the index of the column and update
        # it
        for key in range(len(i)):
            table1.update_column(table_clean[key], element[key])
    # close the file
    table.close()
    # return the result
    return table1


def read_database():
    '''() -> Database
    reads each file and returns a Database object representing the data
    from all csv files in the current directory.
    REQ: File must be a comma-separated file.
    '''
    # set a variable representing Database
    db = Database()
    file_list = glob.glob('*.csv')
    # loop through the file
    for element in file_list:
        # split the .csv extension
        extension = element.split('.')
        # take the file's name
        extension = extension[0]
        # add the information to the dictionary
        db.add_data({extension: read_table(element)})
    return db