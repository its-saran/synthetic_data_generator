import pandas as pd
from .column_generator import Column


class Table():
    def __init__(self):
        self.name = ''
        self.table = pd.DataFrame()

    def create(self, name):
        self.name = name
        self.table = pd.DataFrame()
        return self.table

    def generate_column(self, col_name, nrows, col_type, col_props):
        column = Column()
        if col_type == 'Number':
            if col_props['end'] > nrows:
                col_props['end'] = nrows
            self.table[col_name] = column.generate_number(col_props, self.table)
        elif col_type == 'Date':
            self.table[col_name] = column.generate_date(col_props, self.table)
        elif col_type == 'Text':
            self.table[col_name] = column.generate_text(col_props, self.table)

















# import random

# self.table = pd.DataFrame({
#     'Column 1': [random.randint(3, 9), random.randint(3, 9), 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12],
#     'Column 2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
# })



# # Usage
# table1 = Table()
# table1.generate_column('Date', 'date', {
#     'start': '2020-04-01',
#     'end': '2024-03-31',
#     'freq': 'D'
# })
#
# # Adding a column with text based on count distribution (value not wrapped in a list)
# table1.generate_column('POS', 'text', {
#     'text': ['Website', 'Branches'],
#     'dist': {'type': 'count', 'value': [25, 25]},  # Directly using integer value
#     'count': 50
# })
#
# # Adding a column with text based on ratio distribution (value not wrapped in a list)
# table1.generate_column('POS_Ratio', 'text', {
#     'text': 'Website',
#     'dist': {'type': 'ratio', 'value': 1}  # Directly using integer value
# })
#
