#Please write a Python function, max_num_in_list to return the max number of a
#given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Prints the greatest number in a list"""
    return max(a_list)

m = [1, 45, 3, 8]
max = max_num_in_list(m)
print(max)