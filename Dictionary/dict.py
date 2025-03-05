#  Creating a Dictionary
dict={}

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing values
print(my_dict['name'])  
print(my_dict.get('age'))  

# Adding or updating entries
my_dict['email'] = 'john@example.com'
my_dict['age'] = 26

# Removing entries
del my_dict['city']
email = my_dict.pop('email')
last_item = my_dict.popitem()

# Iterating through a dictionary
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f'{key}: {value}')

# Using dictionary methods
my_dict.clear()
print(my_dict)  # Output: {}


# Creating dictionaries
dict1 = {'name': 'John', 'age': 25, 'city': 'New York'}
dict2 = {}

# 1. clear() - Removes all items

dict1.clear()
print(dict1)  # Output: {}


# 2. copy() - Returns a shallow copy

dict1 = {'name': 'John', 'age': 25}
dict2 = dict1.copy()
print(dict2)  # Output: {'name': 'John', 'age': 25}


# 3. fromkeys() - Creates dictionary from sequence

keys = ['name', 'age', 'city']
value = 'unknown'
dict3 = dict.fromkeys(keys, value)
print(dict3)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}


# 4. get() - Returns value for key

dict4 = {'name': 'John', 'age': 25}
print(dict4.get('name'))  # Output: John
print(dict4.get('city', 'Not Found'))  # Output: Not Found


# 5. items() - Returns key-value pairs

print(dict4.items())  # Output: dict_items([('name', 'John'), ('age', 25)])


# 6. keys() - Returns all keys

print(dict4.keys())  # Output: dict_keys(['name', 'age'])


# 7. pop() - Removes specified key and returns value

dict5 = {'name': 'John', 'age': 25, 'city': 'New York'}
removed_value = dict5.pop('age')
print(f"Removed value: {removed_value}")  # Output: 25
print(f"Dictionary after pop: {dict5}")


# 8. popitem() - Removes and returns last inserted item

last_item = dict5.popitem()
print(f"Removed last item: {last_item}")
print(f"Dictionary after popitem: {dict5}")


# 9. setdefault() - Returns value of key, sets default if key doesn't exist

dict6 = {'name': 'John'}
print(dict6.setdefault('age', 25))  # Output: 25
print(dict6)  # Output: {'name': 'John', 'age': 25}


# 10. update() - Updates dictionary with elements from another dictionary

dict7 = {'name': 'John'}
dict7.update({'age': 25, 'city': 'New York'})
print(dict7)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}


# 11. values() - Returns all values

print(dict7.values())  # Output: dict_values(['John', 25, 'New York'])


# 12. len() - Returns number of items in dictionary

print(len(dict7))  # Output: 3


# 13. in operator - Checks if key exists in dictionary

print('name' in dict7)  # Output: True
print('email' in dict7)  # Output: False


# 14. dict comprehension

squares = {x: x*x for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}