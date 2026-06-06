# игра инвестор
our_products = {"Apple", "Tesla", "McDonald's"}
our_products.discard("Apple")
our_products.discard("Mercedes")
print(our_products)
range_of_company_1 = {"Samsung", "Sony"}
range_of_company_2 = {"Apple", "IBM", "Tesla"}
range_of_company_3 = {"BMW", "Tesla", "Ferrari"}
print(our_products.intersection(range_of_company_1))
print(our_products.intersection(range_of_company_2))
print(our_products.intersection(range_of_company_3))





my_frozenset = frozenset()
print(type(my_frozenset))
my_tuple = tuple() 
print(type(my_tuple))
my_tuple = (0,) 
print(type(my_tuple))
my_tuple = 0,
print(type(my_tuple))
my_tuple = (0) 
print(type(my_tuple))
