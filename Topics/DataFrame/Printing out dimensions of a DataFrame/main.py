import pandas as pd


def print_dim(df):
    data = df.shape
    print('This DataFrame contains {0} rows and {1} columns'.format(data[0], data[1]))


# students_dict = {'First Name': {100: 'Anna',
#                                 200: 'Bob',
#                                 300: 'Maria',
#                                 400: 'Jack'},
#
#                  'Family Name': {100: 'Smith',
#                                  200: 'Jones',
#                                  300: 'Williams',
#                                  400: 'Brown'},
#                  'Age': {100: 21,
#                          200: 20,
#                          300: 25,
#                          400: 22}}
#
# students = pd.DataFrame(students_dict)
# print_dim(students)