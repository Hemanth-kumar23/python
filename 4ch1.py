#dictionary,means key=word , value = meaning ,where we can use any
#all sysntax.it is mutable

info = {
    "key" : "value",
    "name" : "hemm",
    "marks" : 21.1,
    "subjects" : ["python","java","c++"]
}

info["name"] = "monster"
print(info)

#nested dictionary

student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}

print(student["subjects"]["pys"])

#myDict.keys(),retuns all keys

student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}
print(student.keys())


#myDict.value(),returns all value
student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}

print(list(student.values()))

#myDict.items(). returns all (key,val) pairs as tuples 
student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}
print(student.items())

#myDict.get("key").returns the key according to value
student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}

print(student.get("subjects"))


#myDict.update(new update).insert the specified items to the dictionary
student = {
    "name" : "hemm",
    "subjects" : {
        "pys" : 94,
        "chem" : 78,
    }
}

student.update({"city" : "goa"})
print(student)


#set = {}imutable we can use tuple .add,remove,clear.

num = set()
num.add(1)
num.add(34)
num.remove(1)
num.add((1,2,3))
num.clear()
print(num)

#pop.randomly dleate value .

hem = {"hemm","hack","haas" }


print(hem.pop())


#union.where in both set it only print once is know as union.
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))#ans= {1, 2, 3, 4}


#intersection. it will shows what is the common in both sets 

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))#ans= {2,3}