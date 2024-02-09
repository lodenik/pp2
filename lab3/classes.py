# class String:
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input("Enter a string: ")

#     def printString(self):
#         print(self.s.upper())

#S = String()
#S.getString()
#S.printString()


# class Shape:
#     area = 0
#     def printArea(self):
#         print(self.area)
# class Square(Shape):
#     def __init__(self, a):
#         self.side = a
#         self.area = a * a
# x = Square(5)
# x.printArea()


# class Shape:
#     area = 0
#     def printArea(self):
#         print(self.area)
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# x = Rectangle(5, 10)
# x.area()
# x.printArea()


# from math import sqrt
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"Coordinates: ({self.x}, {self.y})")
#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#     def dist(self, other_point):
#         return sqrt((self.x - P2.x) ** 2 + (self.y - P2.y) ** 2)
# P1 = Point()
# P1.move(0, 0)
# P2 = Point()
# P2.move(1, 1)
# P1.show()
# P2.show()
# print(P1.dist(P2))


# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def get_balance(self):
#         print(f'{self.owner} has {self.balance} money')
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
# x = Account("Anton")
# x.deposit(50)
# x.deposit(50)
# x.get_balance()
# x.withdraw(90)
# x.get_balance()
# x.withdraw(20)
# x.get_balance()
# x.withdraw(10)
# x.get_balance()


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# numbers = [2, 4, 6, 9, 11, 13, 17, 20]
# primes = list(filter(lambda x: is_prime(x), numbers))
# print("Prime numbers:", primes)