#Operaters
#1.Arithmetic operaters
num1=10
num2=2
print(num1+num2)#12
print(num1-num2)#8
print(num1*num2)#20
print(num1/num2)#division---float----5.0
print(num1//num2)#floor division---int---quotient---5
print(num1%num2)#modulo division-----remainder----0
print(num1**num2)#power function/exponentiation---100
#2^3=2x2x2=8  3^2=3x3=9  10**2=10^2=10x10=100


num1=9.0
num=6.7
print(num1+num2)



# Assignment Operaters"=,+=,-=,*=,/=,//=,**=,%="

cat=30
print(cat)
cat+=7
print(cat)

# Arithmetic operater
num1=6.5
num2=7.0
print(num1+num2)

# Arithmetic operaters
dog=50
print(dog)
dog+=9
print(dog)

# Comparison operaters(==,!=,<,<=,>,>=)
first=90
second=47
print(second==first)#F
print(first!=second)#T
print(second<first)#47<90 T
print(first<=second)#90<47 or 90=47 F
print(first>second)#F
print(second>=first)#F

#4.Logical Operaters(and,or,not)
first=90
second=47
#and returns True if both of my operands are True
print(first==second and first>0)#F,T---F
print(first!=second and second<0)#T,F---F
print(first>second and second!=first)#T,T---T
print(first<=second and second==first)#F,F---F

#or-returnstrue if one ofmy operands is true
print(first==second or first>0)#F,T----T
print(first!=second or second<0)#T,F---T
print(first>second or second!=first)#T,T---T
print(first<=second or second==first)#F,F-----F

# not-returns the opposite of the result
print(not(first<second))#F---T
print(not(first<=second or second==first))#F----T

#5.Identity operaters(is,is not)
a="apple"
b="ball"
print(a is b)#F
print(a is not b)#T

#6.Membership operaters(in,not in)
s="sample work"
k="work"
print(k in s)#T
print(k not in s)#F
print(s not in k)#T