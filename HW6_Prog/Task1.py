# Написать функцию print_operation_table(operation, num_rows = 9, num_columns = 9)

def print_operation_table(operation, num_rows = 9, num_columns = 9):
    list_row = [i for i in range(num_columns)]
    for j in range(num_rows):
        for i in range(num_columns):
            list_row[i] = operation(j+1, i+1)
            print (str(list_row[i]) + ' '*(5-len(str (list_row[i]))) , end='')
        print()

print_operation_table(lambda x, y: x*y)
print_operation_table(lambda x, y: x*y, 5)
