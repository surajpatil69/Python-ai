l1=[1,"forn",False]
print(l1)

l2=[1,2,3,4,5]
# concate 
print(l2+l1)

print(l1[-1])

#slicing
print(l2[1:4])

l1[2]=True
print(l1)
# we can modify thre list 
l2.pop()
print(l2)


l2.append("dron")
print(l2)

l2.reverse()

l2.insert(1,"baba")
print(l2)


l3=[3,6,9,4,1]
l3.sort()
print(l3)

l4=["baba","dron","raju","mastmastani"]
l4.sort()
print(l4)
l4.sort(reverse=True)

#concatenation

l6=[3,4,5]
l7=["mangu","op"]
print(l6+l7)

#repeat elements 
print(l6*3)
