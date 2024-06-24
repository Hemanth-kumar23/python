#escape sequance character
str = "hey how are you.\ti am fine."
print(str)  


#basic opearter:
#1 concatnation 

a = "hem"
b = "ant"
name = a + b 
print(name)

#length of str.
str1 = "hemmm"
len1 = len(str1)
print(len1)

#index.
str = "apna bahi"
ch=str[3]
print(ch)

#slicing.
str = "hemant kumar"
print(str[0:8]) 

#string fuction.
str = "i am not human bro i sm beast"#check the last letters then give true or false 
print(str.endswith("east"))

str = "i am not human bro i sm beast"#capitalize the first words 
print(str.capitalize())

str = "i am not human bro i sm beast"#to replace ur old char to new.
print(str.replace("a","o"))

str = "i am not human bro i am beast"#to see how many times word is repatie in sentance 
print(str.count("am"))

#if,else,elif.
light = "red"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

#ex=2.
marks = int(input("enter ur grade : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"  
else:
    grade = "D"

print("grade of the student >",grade)


#nesting

age = 34
if(age >= 18 ):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can't drive")

#practice 1

num1 = int(input("enter ur number : "))

rem = num1 % 2
if(rem == 0):
    print("even")
else:
    print("odd")

#practice 2
 
a = int(input("enter ur 1st no : "))
b = int(input("enter ur 2nd no : "))
c = int(input("enter ur 3rd no : "))

if(a >= b and a >= c):
    print("a is greater no : ")
elif(b >= c):
    print("b is gretaer no : ")
else:
    print("c is greater no : ")


#practice 3.
z = int(input("enter ur number : "))
if(z % 7 == 0 ):
    print("mul of 7")
else:
    print("not mul of 7")