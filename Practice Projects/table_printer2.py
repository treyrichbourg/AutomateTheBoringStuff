#! python3
#Write a function that takes a list of lists of strings and displays it in a well-organized table with each column right-justified.

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def table_printer(data):
    #Find the longest string in each column 
    column_widths = [(len(max(column, key=len))) for column in data]
    #Find the length of the columns
    column_length = len(max(data, key=len))
    #Main loop to create our table
    #word will be the element in each nested list
    for word in range(column_length):
        #list to hold our re-arranged list
        column = []
        #index of each nested list/index of our new columns
        for num_of_column in range(len(data)):
            column.append(data[num_of_column][word].rjust(column_widths[num_of_column]))
        print(' '.join(column))

table_printer(table_data)
