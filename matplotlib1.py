import matplotlib.pyplot as plt
import numpy as nps

# xp =nps.arange(1,11)
# print(xp)

# y=3*xp
# plt.plot(xp,y)
# # plt.show()

# plt.title("X vs Y")

# plt.xlabel("x axis")

# plt.ylabel("y axis ")

# plt.plot(xp,y,color='g',linestyle=':',linewidth="5")
# plt.show()
# y1=xp*4
# y2=xp*5
# plt.plot(xp,y1,color="r",linestyle=":")
# plt.plot(xp,y2,color="g",linewidth=5)
# plt.grid(True)
# plt.show()

# # subplots


# plt.subplot(2,1,1)
# plt.plot(xp, y1, color="r", linestyle=":")
# plt.show()
# plt.subplot(2,1,2)
# plt.plot(xp, y2, color="r", linestyle=":")
# plt.show()
# plt.title("X vs Y")
# plt.xlabel("x axis")
# plt.ylabel("y axis ") 
# plt.show()
# # barplot;
# student={"raju":87,"dron":90,"mangu":99,"nody":50}

# name= list(student.keys())
# values =list(student.values())
# plt.bar(name,values)
# plt.title("distribution of marks")
# plt.xlabel("names")
# plt.ylabel("marks")
# plt.show()

# horizontal bar graph 
# plt.barh(name,values)
# plt.title("distribution of marks")
# plt.xlabel("names")
# plt.ylabel("marks")
# plt.show()

#scatter plot
# x=[4,3,2,5,6,7,6,8,9,6]
# y=[5,6,7,8,4,5,3,2,6,5]
# plt.scatter(x,y)
# plt.show()
# # # to change the color
# plt.scatter(x,y,marker="*",c='g',s=100)
# plt.show()
# # size should be the same while ploting
# z=[3,4,5,8,9,6,5,1,3,4]
# plt.scatter(x, y, marker="*", c='r', s=300)
# plt.scatter(x,z,marker=".",c='g',s=100)
# plt.show()

# plt.subplot(1,2,1)
# plt.scatter(x, y, marker="*", c='r', s=300)
# plt.subplot(1,2,2)
# plt.scatter(x,z,marker=".",c='g',s=100)
# plt.show()

# pie chart 
fruits =["apple","mango","banana"]
quantity=[34,55,66]
plt.pie(quantity,labels=fruits)
plt.pie(quantity,labels=fruits,autopct="%0.1f",colors=['yellow','blue','orange'])
plt.show()

# doubnut chart 
plt.pie(quantity, labels=fruits,radius=2)
plt.pie()

