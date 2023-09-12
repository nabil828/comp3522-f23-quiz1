my_dict = {"apple": 3, "banana": 5, "cherry": 2}

# What will be the result of the following code?
my_dict["banana"] += 2
my_dict["kiwi"] = 4
del my_dict["cherry"]

print(my_dict)

# A. {"apple": 3, "banana": 7, "cherry": 2, "kiwi": 4}
# B. {"apple": 3, "banana": 7, "cherry": 2}
# C. {"apple": 3, "banana": 5, "kiwi": 4}
# D. {"apple": 3, "banana": 5, "cherry": None, "kiwi": 4}