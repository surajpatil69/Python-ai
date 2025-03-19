# class phone:
#     def make_call(self):
#         print("making a phone call ")
#     def play_games(self):
#         print("playing pubg")
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_cost(self):
#         return  self.cost
#     def show_color(self):
#         return  self.color

# o1=phone()
# o1.make_call()
# o1.play_games()

# o2=phone()
# o2.set_color("black")
# o2.set_cost("10000")
# o2.show_color()
# o2.show_cost()
# print(o2.show_color())
# print(o2.show_cost())

# creating a class with a constructor
# class employ:
#     def __init__(self,name,age,salary,gender):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender
#     def employee_details(self):
#         print("name of the employee:",self.name)
#         print("age of the employee:",self.age)
#         print("salary of the employee:",self.salary)
#         print("gender of the employee:",self.gender)

# e1=employ("dron",35,100000,"male")
# e1.employee_details()

#inheritance 

# class vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage =mileage
#         self.cost =cost
#     def show_vehicle_detail(self):
#         print("the mileage of vehicle is :",self.mileage)
#         print("the cost of vehicle is :",self.cost)
# v1=vehicle(25,5000)
# v1.show_vehicle_detail()

# class car(vehicle):
#     def show_car_details(self):
#         print("i am a car")

# c1=car(15,5000)
# c1.show_vehicle_detail()
# c1.show_car_details()


# class car(vehicle):
#     def __init__(self, mileage, cost ,color,hp) :
#        super().__init__( mileage, cost)
#        self.color=color
#        self.hp=hp

#     def show_car_details(self):
#         print("color of the car",self.color)
#         print("hp of the car",self.hp)

# c1=car(35,700,"red",8090)
# c1.show_car_details()
# c1.show_vehicle_detail()

# multiple inheritance

# class parent1:
#     def s1(self,str1):
#         self.str1=str1
#     def shows1(self):
#         return self.str1

# class parent2:
#      def s2(self,str2):
#             self.str2=str2
#      def shows2(self):
#         return self.str2

# class child(parent1,parent2):
#          def s3(self,str3):
#                 self.str3=str3
#          def shows3(self):
#            return self.str3

# child1= child()
# child1.s1("i am child of parent1\n")
# child1.s2("i am child of parent2\n")
# child1.s3("i am child of parent3\n")

# child1.shows1()
# child1.shows2()
# child1.shows3()
# print(child1.shows1(),
#       child1.shows2(),
#       child1.shows3())


# multilevel inheritance

class parents:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)

class children(parents):
     def get_age(self,age):
            self.age=age
     def show_age(self):
        print(self.age)

class grandchild(children):
       def get_gender(self, gender):
            self.gender = gender
       def show_gender(self):
        print(self.gender) 

gc=grandchild()
gc.get_name("dron")    
gc.get_age(19)    
gc.get_gender("male")    

gc.show_age()
gc.show_gender()
gc.show_name()