# H.W
# Project:Get the student name and marks, print the total of marks,average and give grades.
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

# if,elif,else
name=input("Enter your marks:")
Math=int(input("Enter your marks:"))
Science=int(input("Enter your marks:"))
Social=int(input("Enter your marks:"))
English=int(input("Enter your marks:"))
total=Science+Math+Social+English
Average=total/5
print("Name:Divya")
print ("total marks:485")
print("Average:97")
if (Average>-90 and Average<-100):
    print("Grade: A")
elif  (Average>-80 and Average<-90):
    print("Grade:B")
elif(Average>-70 and Average<-80):
    print("Grade:C")
elif(Average>-60 and Average<-70):
    print("Grade:D")
print("g")


