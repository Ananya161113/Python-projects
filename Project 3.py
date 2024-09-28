# Project:Find even and odd numbers from a list, and store them separately in a new list
l=[34,5,55,79,57,84,95,47,60]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("the even list is",even)
print("the odd list is",odd)