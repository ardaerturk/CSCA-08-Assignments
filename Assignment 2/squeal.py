from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def split_query(user_input_query):
    '''(str) -> dict
    return the divided query into tokens
    >>> user_input_query = "select i.title,i.rating from imdb,oscar-film \
    where f.year>2010,f.title=f.year"
    >>> split_query(user_input_query)
    {'select': ['i.title', 'i.rating'], 'where': ['f.year>2010', \
    'f.title=f.year'], 'from': ['imdb', 'oscar-film']}
    '''
    # create an empty list and a dict
    query = []
    input_dict = {}
    # split the input query by white space
    user_input_query = user_input_query.split(' ')
    # split the 'where' word if it exists in the input query by using coma
    if 'where' in user_input_query:
        # split where
        input_dict['where'] = user_input_query[5].split(',')
        # split select
        input_dict['select'] = user_input_query[1].split(',')
        # split from
        input_dict['from'] = user_input_query[3].split(',')
    # if not;
    else:
        # split from
        query_dict['from'] = query[3].split(',')
        # split where
        query_dict['select'] = query[1].split(',')
    # return the dict
    return input_dict


def num_of_rows(table):
    '''(Table) -> int
    returns the number of the rows in a table.
    >>> t1 = Table()
    >>> t1.set_dict({'one':[1,2,3],'two':[4,5,6]})
    >>> num_of_rows(t1)
    3
    '''
    #
    parm1 = list(table._table_dict.keys())[0]
    rows = len(table._table_dict[parm1])
    return rows


def cartesian_product(table1, table2):
    '''(Table, Table) -> Table
    return a new table where each row in the first table is paired with
    every row in the second table.
    >>> table1 = {'A': ['B','C'], 'D': ['E', 'F']}
    >>> table2 = {'G': ['H', 'I'], 'J': ['K', 'L']}
    >>> cart_pro = cartesian_product(table1, table2)
    >>> cart_pro == {{'J': ['K', 'L', 'K', 'L'], 'G': ['H', 'I', 'H', 'I'], \
    'A': ['B', 'B', 'C', 'C'], 'D': ['E', 'E', 'F', 'F']}}
    True
    >>>table1 = {'A': [], 'B': []}
    >>>table2 = {'D': [], 'D': []}
    >>>cart_pro = cartesian_product(table1, table2)
    >>> cart_pro == {'D': [], 'A': [], 'B': []}
    True
    '''
    # create a dictionary for the new table
    table = dict()
    # loop through the table1
    for element in table1:
        table[element] = []
        # find its length
        length_table1 = len(table1[element])
    # loop through the other table
    for element in table2:
        table[element] = []
        # find its length
        length_table2 = len(table2[element])
    # go through the tables to pair it with the other table
    for element in range(length_table1):
        for i in range(length_table2):
            # pair the each row with the other one
            for elements in table1:
                table[elements].append(table1[elements][element])
            for elements in table2:
                table[elements].append(table2[elements][i])
    # return the dictionary that created initialy
    return table


def after_from(tokens, pos_from):
    '''(list of str) -> list of str
    given the query return the tables after 'from'
    '''
    # create an empty list
    res = []
    # split the columns if there are more than one
    if (',' in tokens[pos_from]):
        # split it in list
        res = tokens[pos_from].split(',')
    # if not;
    else:
        # add it into the list directly
        res.append(tokens[pos_from])
    # return result
    return result


def from_token(Database, query):
    '''(Database,dict) -> Table
    Return a table that is in the from list and combine the tables with
    cartesian_product.
    '''
    # find 'from' in the list
    query_from = query['from']
    #  use database class to get dictionary representation
    db = Database.get_dict()
    table1 = db[query_from[0]]
    # loop through the tables to get cartesian product, tables to combine
    # tables
    for element in range(1, len(query_from)):
        table2 = db[query_from[element]]
        # get the cartesian-product
        table1 = cartesian_product(table1, table2)
    # return result
    return table1


def token_select(cartesian_table, token_dict):
    '''(Table, dict) -> Table
    create a new table by finding the values of 'select' and find the index
    value to match them within the table.
    '''
    list_token = token_dict["select"]
    # use cartesian table to get the dict
    cartesian_table = cartesian_table.get_dict()
    # create a new dict
    select_dict = {}
    # set a variable as a new table
    table = Table()
    if list_token == ["*"]:
        list_token = list(cartesian_table.keys())
    for element in list_token:
        select_dict[element] = cartesian_table[element]
    # set dictionary to the table
    table.set_dict(select_dict)
    # return table
    return table


def del_cols(table, column):
    '''(Table, int) -> Table
    Return a table with deleted colums which are not selected in the given\
    query
    '''
    if column[0] == '*':
        # set it as a list
        column = list(table._table_dict.keys())
    # loop through the list
    for element in list(table._table_dict.keys()):
        # if the column is not in the column list
        if element not in column:
            # delete the columns
            table.delete_colm(element)
    # return result
    return table


def run_query(database, user_input_query):
    '''(Database, str) -> Table
    Given user_input-query on the database, return the result table by using\
    cartesian product
    '''
    # get the divided tokens
    user_dict = split_query(query)
    # get the cartesian_table by using from_token function
    cartesian_table = from_token(Database, user_dict)
    # combine the functions
    result = token_select(cartesian_table, user_dict)
    # return result
    return result


if(__name__ == "__main__"):
    '''
    asks for queries and prints the table
    example form: select *column(s)* from *Tables*
    where *column>/=column*/*column>/=value*
    '''
    # read the database
    database = read_database()
    # ask the input
    query = input("Enter a SQuEaL query, or a blank line to exit: ")
    # keep ask the input if the answer is not blank
    while (query != ''):
        # print the tables
        Table.print_csv(run_query(database, query))
        # ask for input
        query = input("Enter a SQuEaL query, or a blank line to exit: ")