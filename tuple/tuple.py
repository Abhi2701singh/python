""" creating a tuple """

emp_tuple=() # empty tuple
print(emp_tuple)
my_tuple=(12,"hello",3.14) # tuple with multiple elements
print(my_tuple)

a=10,20,30   # tuple without parentheses(implicit tuple)
print(a)
print(a[1])

single_elem=(5,)
print(single_elem)

""" ----------- slicing ------------  """

t=(10,20,30,40,50,60,70,80,90,100)

print(t[1:4]) # element index 1 to 3
print(t[:4]) # first 4 element
print(t[::2]) # every second element
print(t[::-1]) # reverse tuple

""" ------- tuple method --------- """

x=(1,2,3,4,5,6,7,8,9,1,2,3,4,5,2)

print(x.count(2)) 
print(x.count(3))
print(x.count(9))


print(x.index(2))
print(x.index(6))
print(x.index(9))

""" -------- tuple operation ------------ """

# ----------- concatenation

t1=(1,2,3)
t2=(4,5,6)
result=t1+t2
print(result)

# repeatiton

t3= (1,2,3)

print(t3*4)

#  ----------- membership test

t4=(10,20,30,40)

print(20 in t4)
print(20 not in t)

""" ---------- nested tuple  --------  """

nested_tuple = ((1, 2, 3), ("A", "B", "C"))
print(nested_tuple[0])  
print(nested_tuple[1][2]) 


""" ----------- List to Tuple ---------- """

l = [1, 2, 3]
t = tuple(l)
print(t)  

""" ------------ Tuple to List ------------- """

t = (10, 20, 30)
l = list(t)
print(l)  


""" ------------- Tuples in a Dictionary ----------- """

students = {
    ("Abhi", 101): "A",
    ("Aman", 102): "B",
    ("Amol", 103): "c"
}

print(students[("Abhi", 101)]) 



""" -------- THE END ------"""