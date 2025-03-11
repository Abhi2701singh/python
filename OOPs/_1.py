# --------- Oops -------- #

# class student:
#     name="abhinav"
#     age=20

# #creating object of class
# s1=student()
# print("name ->",s1.name)
# print("age ->",s1.age)

# class car:
#     color="red"
#     speed=200
#     brand="BMW"

# c1=car()
# print("color ->",c1.color)
# print("speed ->",c1.speed)
# print("brand ->",c1.brand)

"""  __init__ function  """

# class student:
#     def __init__(self):
#         print("hello")

# s1=student()  


# class student:
#     def __init__(self, fullname):
#         self.name=fullname

# s1=student("abhinav")
# print(s1.name)          

# s2=student("singh")
# print(s2.name)


# class student:
#     def __init__(self, fullname ,marks):
#         self.name=fullname
#         self.marks=marks
# s1=student("abhinav",84)
# print(s1.name,s1.marks)          

# s2=student("amol",80)
# print(s2.name, s2.marks)


"""  class & instance attribute  """

# class student:
#     college="UIT" #class attribute
#     def __init__(self,name,coures):
#         self.name=name   # instance attribute
#         self.course=coures

# s1=student("abhinav","B.tech")
# print(s1.name,s1.course,s1.college)
# # or
# print(s1.name,s1.course,student.college)


"""  method [methods are function that belong to object] """

# class student:
#     def __init__(self,fullname):
#         self.name=fullname
#     def hello(self):
#         print("hello",self.name)


# s1=student("abhinav")
# s1.hello()


"""  Q-1 create student class that take name & marks of 3 subjects as arguments in constructor. then create a method to print the average."""

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum=sum+i
#         print("hi",self.name,"your avg score is",sum/len(self.marks))

# s1=student("abhinav",[80,90,85])
# s1.average()


""" static method [methods that don't use the self parameter(work at class level)]  """

# class student:
#     @staticmethod
#     def hello():
#         print("hello")
# s1=student()
# s1.hello()



"""  Abstraction [ hiding the implementation details of a class and only showing the essential features to the user ]  """

# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("car is started")
# car1=car()
# car1.start() 


"""  Encapsulation [ wrapping up of data into a single unit ]  """


""" Q-2 create account class with 2 attribute-balance & account no. create method for debit, credit and printing the balance. """

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    # debit method
    def debit(self,amount):
        self.balance=self.balance-amount
        print("Rs.",amount,"was debited from your account.")
    def credit(self,amount):
        self.balance=self.balance+amount
        print("Rs.",amount,"was credited to your account.")

    def print_balance(self):
        print("your balance is",self.balance)


acc1=account(1000,123456789)
print(acc1.balance,acc1.account_no)
acc1.credit(200)
acc1.print_balance()
acc1.debit(600)
acc1.print_balance()
acc1.credit(200)
acc1.print_balance()
