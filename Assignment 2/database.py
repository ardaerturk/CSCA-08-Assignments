class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self):
        '''(Table) -> NoneType

        Create a new table with 0 cloums and 0 rows
        '''
        self._table_dict = {}

    def table_add_column(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType
        Add a column to the table
        '''
        self._table_dict.update(new_dict)

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType
        Populate this table with the data in new_dict.
        '''
        # use for loop to add data
        for element in new_dict.keys():
            self._table_dict[element] = new_dict[element][:]

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}
        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._table_dict

    def update_column(self, column, text):
        '''(Table, str, list of str) -> NoneType
        Update the column with the text.
        REQ: The column must be exist.
        '''
        self._table_dict[column].append(text)

    def title_column(self):
        '''(Table) -> list of str
        returns the the names of the columns in the table in list
        '''
        return [self._table_dict.keys()]

    def delete_colm(self, index):
        '''(Table, int) -> NoneType
        deletes the ith column'''
        self._table_dict(index)

    def num_rows(self):
        '''(Table) - > int
        returns the number of rows
        '''
        # set the counter to zero and use for loop to get the number of rows
        index = 0
        for element in self._table_dict:
            index = len(self._table_dict[element])
        return index

    def get_col(self):
        '''(Table) -> list of str
        returns the colums
         '''
        return [self._table_dict.keys()]

    def get_row(self, index):
        '''(Table, int) -> dict of str
        returns the row at a given index
        '''
        row_dict = {}
        get_dict = self._table_dict

        # use for loop to get the data on row
        for element in self.get_col():
            row_dict[element] = get_dict[element][index]

    def pop_table(self, table):
        '''(Table, Table) -> NoneType
        adds the table with the other table'''
        # loop through the table to add the data
        for element in table._table_dict.keys():
            self._table_dict[element] = table._table_dict[element][:]

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))


class Database():
    '''A class to represent a SQuEaL database'''

    def __init__(self):
        '''(Table) -> NoneType'''
        self._datadict = {}

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        '''
        self._databasedict = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._datadict

    def add_data(self, new_table):
        '''(Database, dict of {str: Table}) -> NoneType
        add a new table to the database
        '''
        self._datadict.update(new_table)

    def titles(self):
        '''(Database) -> list of str
        returns the titles in the table in the database
        '''
        return [self._datadict.keys()]