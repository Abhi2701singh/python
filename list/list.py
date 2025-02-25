# List -> a collection of similar or different types of data items.
# a list is created by placing item inside [] separated by commas.


empty_list=[] # empty list

num=[1,2,3,4,5,6,7,8,9,10]
print(num)

num2=[1,2,"abhi",'amol',3.14,True] # mixed list
print(num2)

"""   Accessing element in a list   """

fruits=["apple","banana","cherry"]

print(fruits[0]) # O/p = apple
print(fruits[2]) # O/p = cherry

print(fruits[-2]) # O/p = banana

"""  list slicing """

num=[1,2,3,4,5,6,7,8,9,10]

print(num[1:4]) # output [2,3,4]
print(num[:5])  # output [1,2,3,4,5] 
print(num[::2]) # output [1,3,5,7,9]
print(num[-3:]) # output [8, 9, 10]
print(num[-1:]) # output [10]

"""  modifying list """

fru=["apple","banana","cherry"]
print(fru)  # output ['apple', 'banana', 'cherry']
fru[1]="mnago"
print(fru)  # output ['apple', 'mnago', 'cherry']


""" adding elemens to a list """

# 1- append() -> add an element to the end.

num=[2,3,5,6,7,9]
print(num)  # output [2, 3, 5, 6, 7, 9]
num.append(10)
print(num)  # output [2, 3, 5, 6, 7, 9, 10]

# 2- extend() -> add multiple element

num=[10,12,14]
print(num)   #output [10,12,13]

num.extend([40,50,60])
print(num)   #output [10,12,13,40,50,60]

# 3- insert() -> insert at a specific index

num=[20,30,"abhi",50]
print(num) # # output  [20, 30, 'abhi']
num.insert(2,"abhinav")
print(num)   # output  [20, 30, 'abhinav', 'abhi', 50]


"""  remove element from a list """

# 1- remove() -> remove the first occurrence of a value

num=["a","b","c","d","a"]
num.remove("a")
print(num)  # output ['b', 'c', 'd', 'a']

# 2- pop() -> remove an item by index (default is the last element)

num=["abc","def",2,4.56,"hii"]
num.pop()
print(num) # output ['abc', 'def', 2, 4.56]

num.pop(1)
print(num) # output ['abc', 2, 4.56]

# 3- del() -> delete an element or the entire list.

x=["abc","def",2,4.56,"hii"]
del x[2]
print(x)  # output ['abc', 'def', 4.56, 'hii']

"""  looping through a list """

# 1- for loop
fruit=["apple","banana","mango"]
for i in fruit:
    print(i,end=" ")  #output -> apple banana mango

# 2- while loop

fruit=["apple","banana","mango","cherry"]

s=0
while s<len(fruit):
    print(fruit[s],end=" ") # output apple banana mango cherry
    s=s+1

# 3- using list comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


"""  sorting a list """

# 1- sort() –> Modifies the list.

numbers = [4, 2, 9, 1, 5]

numbers.sort()  
print(numbers)  # Output: [1, 2, 4, 5, 9]


# 2- sorted() –> Returns a new sorted list.

numbers = [4, 2, 9, 1, 5]

numbers = sorted(numbers, reverse=True)
print(numbers)  # Output: [9, 5, 4, 2, 1]

  # or

numbers.sort(reverse=True)
print(numbers)

""" List Operations """

# 1- Concatenation (+)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# 2- Repetition (*)

repeated = [1, 2, 3] * 2
print(repeated)  # Output: [1, 2, 3, 1, 2, 3]


# 3- Checking Membership (in)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True


"""  Nested Lists (2D Lists)  """

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])  # Output: 6

matrix = [[1, 2, 3], [4, ["abhinav","singh"], 6], [7, 8, 9]]

print(matrix[1][1][0])  # Output: abhinav

"""  Copying a List """

original = [1, 2, 3]
copy_list = original.copy()  # or original[:]
copy_list.append(4)

print(original)  # Output: [1, 2, 3] (Unchanged)
print(copy_list)  # Output: [1, 2, 3, 4]

x = [1, 2, 3, 4]
copy_x = x[:]  # or original.copy()
copy_x.append("abhi")

print(x)  #output [1, 2, 3, 4](original)
print(copy_x)  # output [1, 2, 3, 4, 'abhi']


"""   Converting Other Data Types to Lists  """

string = "hello"
print(list(string))  # Output: ['h', 'e', 'l', 'l', 'o']

tuple1 = (1, 2, 3)
print(list(tuple1))  # Output: [1, 2, 3]


""" Using enumerate() with Lists"""
#If you need both the index and value while looping through a list, enumerate() is useful.

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

""" Using zip() with Lists """
#The zip() function combines multiple lists element-wise.

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output:
# Alice scored 90
# Bob scored 85
# Charlie scored 95

""" Filtering Lists Using filter()"""
#The filter() function filters elements based on a condition.


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


""" Mapping Lists Using map() """
# The map() function applies a function to all elements.

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


"""List Flattening (Nested Lists to Single List) """
# When you have a nested list, and you want to convert it into a single list.


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


""" Removing Duplicates from a List  """
#If you want to remove duplicates, you can convert the list into a set and back into a list.


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))

print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

# For order-preserving removal:
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)  # Output: [1, 2, 3, 4, 5]
""" Using collections.deque for Faster List Operations """
# Lists have slow insert() and pop(0) operations. The deque (double-ended queue) from collections is faster.


from collections import deque

queue = deque([1, 2, 3])
queue.append(4)  # Faster than list append()
queue.popleft()  # Faster than list pop(0)

print(queue)  # Output: deque([2, 3, 4])
""" List Comparison """
# You can compare two lists using == or is.


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # True (Same elements)
print(list1 is list2)  # False (Different memory locations)
print(list1 is list3)  # True (Same reference)


""" Finding the Most Frequent Element """


from collections import Counter

numbers = [1, 2, 3, 1, 2, 1, 3, 1]
count = Counter(numbers)

most_common = count.most_common(1)  # Returns most frequent element
print(most_common)  # Output: [(1, 4)]


""" Rotating a List """
# You can rotate a list by moving elements left or right.

def rotate_right(lst, n):
    n = n % len(lst)  # Handle large shifts
    return lst[-n:] + lst[:-n]

numbers = [1, 2, 3, 4, 5]
rotated = rotate_right(numbers, 2)
print(rotated)  # Output: [4, 5, 1, 2, 3]
""" List Intersections (Common Elements)"""

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))
print(common)  # Output: [3, 4]


""" Reversing a List in Different Ways"""
#Method 1: Using reverse()

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

#Method 2: Using Slicing

numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
