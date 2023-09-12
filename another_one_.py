def modify_dict(my_dict):
    my_dict.update({"key1": "value1"})
    my_dict = {"new_key": "new_value"}
    

original_dict = {"key0": "value0"}
modify_dict(original_dict)

print(original_dict)

# What will be the value of 'original_dict' after executing this code?

# A. {"key0": "value0", "key1": "value1"}
# B. {"new_key": "new_value"}
# C. {"key0": "value0"}
# D. {"key0": "value0", "new_key": "new_value"}