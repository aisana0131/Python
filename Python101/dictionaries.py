my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# print(my_dict)
my_dict['country'] = 'USA'
# print(my_dict)
# {'name': 'John', 'age': 25, 'city': 'New York'}
# {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
#  to change the value - we just simply overwrite the value: 
my_dict['age'] = '35'
# print(my_dict)
# output: {'name': 'John', 'age': '35', 'city': 'New York', 'country': 'USA'}

# for item in my_dict.values():
    # print(item)
# output: John
#         35
#         New York
#         USA


# del my_dict['age']  This will delete age from the list
# print(my_dict)

