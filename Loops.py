# # # loops-to repeat a task multiple times
# # # # for loop
# # # name="Ananya"
# # # for a in name:
# # #     print(a)
# # #
# # # # range(start,stop,step)
# # # # range(1,5)-1,2,3,4
# # # # range(1,11)-1,2,3,4,......10
# # # # range(1,11,2)-1,3,5,7,9
# # #
# # # for a in range(1,7):
# # #     print(a)
# # # for a in range(25,55,4):
# # #     print(a)
# # #
# # # for a in range(6):
# # #     print(a)
# # #
# # #     # Hw: Calculate
# # #     # the
# # #     # sum
# # #     # of
# # #     # first
# # #     # n
# # #     # natural
# # #     # numbers
# # # # Get 3 numbers from user for 5 times and print the product of it.
# # #
# # # # H.W-1
# # # n=int(input("Enter a number :"))
# # # a=0
# # # for i in range(1,n+1): #(1,2,3,4,5)
# # #     a=a+i
# # # print("Sum of natural numbers is ",a)
# # # # H.W-2
# # #
# # # a1=int(input("Enter 1st number :"))
# # # a2=int(input("Enter 2nd number :"))
# # # a3=int(input("Enter 3rd number :"))
# # # print("Product of a1, a2, a3 is :",(a1*a2*a3))
# # #
# # #
# # # for i in range(1,10):
# # #     if i%2==0:
# # #         print("Even number ",i)
# # #     else:
# # #         print("Odd number ",i)
# # #
# # # # nested for loop
# # # # list[]
# # # # tuple()
# # #
# # # # colors=["purple","pink","orange","blue"]
# # # # for i in colors:
# # # #     print(i)
# # #
# # # colors=["pink","purple","blue","orange"]
# # # vegetable=["beetroot","cabbage","turnip","carrot"]
# # # for i in colors:
# # #     for j in vegetable:
# # #         print(i,j)
# # #
# # # for i in range(1,4):
# # #     for j in range(1,6):
# # #         print("Row-",i,"Column-",j)
# # #
# # # # Pattern printing
# # # # Square pattern
# # # for i in range (3):
# # #     for j in range (3):
# # #         print("*",end=" ")
# # #     print()
# # #
# # # # Rectangle pattern
# # # for i in range (3):
# # #     for j in range (8):
# # #         print("*",end=" ")
# # #     print()
# # #
# # # # Triangle pattern
# # # size=int(input("Enter a number: "))
# # # for i in range(size):
# # #     for j in range(i+1):
# # #         print("*",end=" ")
# # #     print()
# # # # Reverse triangle
# # # a=int(input("Enter a number:"))
# # # for i in range(a,0,-1):
# # #     for j in range(i):
# # #         print("*", end=" ")
# # #     print()
# # # #
# # #  # Break:
# # # for i in range(1,14):
# # #      if i==12:
# # #          break
# # #      else:
# # #          print(i)
# # # skip and move
# #
# # #
# # #  l=[2,4,6,8,9,10]
# # #  for i in l:
# # #      if i%2==0:
# # #          print("An odd number is found")
# # #          break
# # #      else:
# # #          print("even",i)
# #
# # #Continue
# # for i in range(1,17):
# #     if i==13:
# #         continue
# #     else:
# #         print(i)
# #         # start from the if.continue from the if value
# #
# #
# #
# # p=[70,-30,-90,11,5]
# # for i in p:
# #     if i<0:
# #         continue
# #     else:
# #         print(i)
#
#
#
# # pass
# # for i in range(1,35):
# #     if i<=20:
# #         pass
# #     else:
# #         print(i)
#         # H.W
#         # give examples for pass,continue,break
#         # revise loops
#
# # H.W
# # Continue
# # for i in range(1,30):
# #     if i==15:
# #         continue
# #     else:
# #         print(i)
# #
# #
# # # Break:
# # for i in range(1,14):
# #      if i==12:
# #          break
# #      else:
# #          print(i)
# #
# # # pass
# # for i in range(1,45):
# #     if i<=20:
# #         pass
# #     else:
# #         print(i)
#
#
# # While loop
# # Number of iterations is unknown
# # Will execute a code as long asa condition is True
# # 1,2,3,4.....................50
# # i=1
# # while i<=50:
# #     print(i)
# #     i+=1
# #
# #
# # # Print the series 10,20,30,....,200
# # i=10
# # while i<=200:
# #     print(i)
# #     i+=10
# #
# # # 50 to 25 in desending order
# # i=50
# # while i>=25:
# #     print(i)
# #     i-=1
# #
# # # print the series 500,450,400,.....,50
# # i=500
# # while i>=50:
# #     print(i)
# #     i-=50
#
#  # p='Ananya'
#  # up=input("Enter your password :")
#  # while up!=p:
#  #     print("Wrong password")
#  #     up=input("Enter your password :")
#  # print("Correct password")
#  # # password ^ do completely in new file project

#
#  # Multiplication tables
# num=int(input("Enter a number to print that table: "))
# # 5x1=5  5x2=10...
# i=1
# while i<=15:
#     print(num,"x",i,"=",i*num)
#     i+=1
#
# Nested while
#  3 students,5 subjects
# a=1
# while a<=3:
#     Name=input("Enter the student name : ")
#     Std=int(input("Enter the standard : "))
#     total=0
#     b=1
#     while b<=5:
#         marks=int(input("Enter your marks to add : "))
#         total+=marks
#         b+=1
#     print("The total of",Name,"is",total)
#     print(40*'*')
#     a+=1

# H.W
# Print multiplication tables from 1 to 10 using nested while.
# num=1
# while num<=10:
#     c=1
#     while c<=15:
#         print(num,"X",c,"=",c*num)
#         c+=1
#     num+=1
# Lists []
# collection
# mutable-changeable
# ordered
#
# l=[12,7.76,"cat",5,7,"ball",456]
# # 0     1    2   3 4    5     6
# print(l)
# print(type(l))
# # Indexing
# print(l[5])
# print(l[1])
# #
# # slicing[start:stop:step]
# print(l[1:6])
# print(l[2:5])
# print(l[1:6:2])
# print(l[:5])
#
# # length
# print(len(l))
# # append()
# l.append("Ananya")
# print(l)
# l.append(100)
# print(l)
# # insert
# l.insert(2,"ananya")
# print(l)
# # extend
# l.extend([7,"ball",456])
# print(l)
# l=[12,79.807,"pen",12,99,"cat",45690]
# # remove
# l.remove(12)
# print(l)
# # pop(index)
# l.pop(3)
# print(l)
# l.pop()
# print(l)
# # index
# print(l.index("cat"))
# l=[12,79.807,"pen",12,99,"cat",45690]
# # count()
# print(l.count(99))
# # reverse()
# l.reverse()
# print(l)
# a=[78,37,35,96,57,58,86,39,47,85]
# # sort
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# # Max,min
# print(max(a))
# print(min(a))
# s=["wind","water","fire","earth","sky","life"]
# # s.sort()
# # print(s)
# s.clear()
# print(s)
# # replace
# s[3]="Ananya"
# print(s)
# Project:Find even and odd numbers from a list, and store them separately in a new list


   














