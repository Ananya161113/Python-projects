# Conditional Statement
# If and Else
a=int(input("enter a value:"))
if (a>0):
    print("This is a positive number")
else:
    print("This is not a positive number")


# get the name and age from user, and check the
# user eligible to vote or not
# # Find out the climate, if it is hot, print "cant play
# games", if it is cool,
# # "jolly, we can play games"
climate=(input("enter the climate:"))
if ("hot"):
    print("can't play games")
else:
     print("jolly we can play games")



# Get input from the user as age if the age is 65 or older, it considers the user a senior citizen.
# If age is lesser than 0,it considers it invalid
# If the age is between 0 and 17 (inclusive), it considers the user a minor.
# If the age is between 18 and 64 (inclusive), it considers the user an adult.

# Get the age from user,
# if age is less than 18, print "you are not eligible"
# if age is greater than 18 and less than 60,
# Print"you are eligible to attend the event"
# if age is above 60, print"you are too old ,
# so not able to attend the event"

    # Checking if a
    # number is both
    # positive and even
    # using
    # logical
    # operator


age=int(input("Enter the age : "))
if(age<=0):
    print("The age is invalid")
elif(age>=65):
    print("Senior citizen")
elif(age>0 and age<=17):
    print("Minor")
else:
    print("Adult")



age=int(input("Enter the age : "))
if(age<18):
    print("you are not eligible")
elif(age>=18 and age <=60):
    print("you are eligible to attend the event")
else:
    print("you are too old, so not able to attend the event")


num=int(input("Enter any positive or negative number : "))
if(num<=0):
    print("The number is not positive")
elif(num>0 and num%2==0):
    print("The number is positive and even")
else:
    print("The number is not even")