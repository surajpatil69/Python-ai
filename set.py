# this is the data structures that we can not access with the index
# used to store unique element
s1={1,"apple",True}
print(s1)

# print(s1[0])# error

# We can not also have duplicate element 

s2={1,1,1,1,1,True,True}
print(s2)

s2.add("loki")

s1.update([20,40,60])# it will always print the element in unordered manner 
print(s1)

s2.remove("loki")
print(s2)


#Union in set 

s1={1,2,3,4,5}
s2={5,6,7,8}
s1.union(s2)
print(s1.union(s2))

# intersection in set 
print(s1.intersection(s2))
