# 🚀 Python Dictionary - Complete Guide

Welcome to the **Python Dictionary** repository! This repository contains detailed explanations and code examples to help you master **dictionaries** in Python. A dictionary is a powerful data structure that allows efficient storage and retrieval of key-value pairs. 🏆

## 📌 What is a Dictionary?
A **dictionary** in Python is an unordered, mutable collection of **key-value pairs**. It provides fast lookups and is widely used in various applications, such as data storage, JSON parsing, and caching.

## ✨ Features of Dictionary
✅ Stores data in **key-value** pairs  
✅ **Keys** must be immutable (strings, numbers, tuples)  
✅ **Values** can be of any data type  
✅ Supports **fast lookups, insertions, and deletions**  
✅ Maintains **insertion order** (Python 3.7+)  
✅ Dynamic and flexible data storage  

---
## 🔥 Dictionary vs Other Data Structures
| Feature       | Dictionary (`dict`) | List (`list`) | Tuple (`tuple`) | Set (`set`) |
|--------------|------------------|------------|--------------|-----------|
| **Mutable?** | ✅ Yes            | ✅ Yes     | ❌ No        | ✅ Yes    |
| **Ordered?** | ✅ (Python 3.7+)  | ✅ Yes     | ✅ Yes       | ❌ No     |
| **Key-Value?** | ✅ Yes            | ❌ No      | ❌ No        | ❌ No     |
| **Fast Lookup?** | ✅ Yes            | ❌ No      | ❌ No        | ✅ Yes    |

---
## 📂 How to Use
Follow these steps to get started with dictionary examples in Python:

```sh
# Clone the repository
git clone https://github.com/Abhi2701singh/python.git

# Navigate to the Dictionary folder
cd python/Dictionary

# Open the Python file
type dict.py  # For Windows
cat dict.py   # For macOS/Linux
```

---
## 📜 File Overview
🔹 [`dict.py`](https://github.com/Abhi2701singh/python/blob/main/Dictionary/dict.py) – Contains Python code demonstrating various dictionary operations such as creation, access, modification, and iteration. 🎯

---
## 📝 Dictionary Operations in `dict.py`
### 📌 Creating a Dictionary
```python
dict = {}

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```
### 🔍 Accessing Values
```python
print(my_dict['name'])  
print(my_dict.get('age'))  
```
### ✏️ Adding or Updating Entries
```python
my_dict['email'] = 'john@example.com'
my_dict['age'] = 26
```
### ❌ Removing Entries
```python
del my_dict['city']
email = my_dict.pop('email')
last_item = my_dict.popitem()
```
### 🔄 Iterating Through a Dictionary
```python
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f'{key}: {value}')
```
### 🔥 Dictionary Methods
```python
# clear()
my_dict.clear()
print(my_dict)  # Output: {}

# copy()
dict2 = my_dict.copy()

# fromkeys()
keys = ['name', 'age', 'city']
dict3 = dict.fromkeys(keys, 'unknown')

# get()
print(my_dict.get('name', 'Not Found'))

# items()
print(my_dict.items())

# keys()
print(my_dict.keys())

# pop()
removed_value = my_dict.pop('age', 'Key not found')

# popitem()
last_item = my_dict.popitem()

# setdefault()
my_dict.setdefault('age', 25)

# update()
my_dict.update({'city': 'Boston'})

# values()
print(my_dict.values())

# len()
print(len(my_dict))

# in operator
print('name' in my_dict)

# Dictionary comprehension
squares = {x: x*x for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
---
## 🤝 Contributions
Contributions are welcome! If you have improvements or additional examples, feel free to **fork** this repository, make changes, and submit a **pull request**. Let's make this resource even better! 🚀

---
## 📄 License
This project is **open-source** and available under the **MIT License**.

💡 _Happy Coding!_ 💡

