#sring,float,intger.

name=input("what is your name ?:")
age=int(input("how old are you?:"))
height=float(input("how tall are you ?:"))
print("hello "+name)
print("you are "+str(age)+"year old")
print("your are "+str(height)+"cm tall")

#ex 2.
name = input("enter ur name : ")
age = int(input("enter ur age : "))
sal = float(input("enter ur sal : "))

print("wlecome",name,"so ur age is :",age,"what is ur sla per year",sal)

# if,elif,else

#1st example: 

light = input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#2st example:

marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
else:
    print("D")

#conditional staement, single if/ternary operate  

food = input("food : ")
eat = "yes"if food == "cake" else "no"
print(eat) 

#ex 2

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


#arithmetic operation:

a = 10 
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a % b )# reminder 
print(a ** b)# a^b

#relation operators 

a = 50 
b = 20

print(a == b)
print( a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#assigment operators 

num = 10
num += 10 #: +=,-=,*=,/=,5=,**=
print("num :", num)

#type conversion 

a = 5
b = 2.5
sum = a + b
print(a + b)

#typecast

a = int("5")
b = 2.5
sum = a + b
print(sum)