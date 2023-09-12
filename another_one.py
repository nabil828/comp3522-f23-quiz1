# Consider the following code:

def modify_list(my_list):
    my_list.append(5)
    my_list = [1, 2, 3, 4]

original_list = [10, 20, 30]
modify_list(original_list)

# What will be the value of 'original_list' after executing this code?

# A. [10, 20, 30, 5]
# B. [1, 2, 3, 4]
# C. [10, 20, 30]
# D. [1, 2, 3, 4, 5]