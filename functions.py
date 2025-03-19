def fun1():
    print("hello ")

fun1()

def add(i):
    return i+5
add(10)
print(add(10))

def odd_even(x):
    if x%2==0:
        print("x is even")
    else:
        print("odd")

odd_even(10)

#lambda function 
# y=lambda x:x*x*x
# y(5)
# print(y(5))

# #lambda with filter 
# l1=[1,2,4,5,6,7,8]
# l2= list(filter(lambda x:(x%2!=0),l1))
# print(l2)
 
