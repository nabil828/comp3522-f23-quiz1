data = "John:35|Alice:28|Bob:42|Eve:19"

# What will be the result of the following code?
entries = data.split("|")
person_dict = {}
for entry in entries:
    name, age = entry.split(":")
    person_dict[name] = int(age)

names = ", ".join(person_dict.keys())
print(names)

# ["John", "Alice", "Bob", "Eve"]
# "John:35, Alice:28, Bob:42, Eve:19"
# "John, Alice, Bob, Eve"
# {"John": 35, "Alice": 28, "Bob": 42, "Eve": 19}

# Answer: "John, Alice, Bob, Eve"