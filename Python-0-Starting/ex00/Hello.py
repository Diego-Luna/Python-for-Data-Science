ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# * Modify the list
ft_list[1] = "World!"

# * Tuples are immutable, so we create a new tuple
ft_tuple = (ft_tuple[0], "France!")

# * Modify the set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# * Modify the dictionary
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
