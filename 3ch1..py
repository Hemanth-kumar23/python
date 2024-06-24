#list and tuples. 

marks = ["karan",27,"banglore"]
print(marks[0])

#mutable=we can change our data
marks[2] = "goa"
print(marks)


#slicing.
marks = [23,48,59,30]
print(marks[0:2])
#it simlar to negative slicing

#list method.#append
LIST = [12,17,18,10]
LIST.append(45)#add one element at the last.
print(LIST)

#sort.ascending order.
list = [12,17,18,10]
print(list.sort())#ascending order 
print(list)

#sort,descending order.

list = [12,17,18,10]
print(list.sort(reverse=True))#descending order.
print(list)

#reverse.

list = [12,17,18,10]
list.reverse()#reverse the whole list
print(list)

#insert.

list = [2,1,3]
list.insert(1,5)#insert the value after no.
print(list)


#remove 

list = [2,1,3]
list.remove(1)#remove the first no which no is enetred.
print(list)


#pop

list = [2,1,3]
list.pop(1)#it removes specific no.
print(list)


#tuples.
tup = (1,2,3,4,5,6,7)
print(tup[0])

#index

tup = (2,1,3,1)
print(tup.index(1))# index count the first digit 

#count

tup = (1,2,3,4,4,4)
print(tup.count(4)) #count totally how many times repate.


#practice question.


#practice question2.

list1 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome") 

#practice 2.

grade = ["C","D","A","A","B","B","A"]

print(grade.count("A"))

#practice 3.

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)