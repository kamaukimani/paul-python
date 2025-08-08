# initializer: constructor
#special  method in a class
#initializer: method is called whenever the blueprint is used
#to create an object
#method function is inside a class

# method your create you have to have the self:keyword
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

# def my_deco(fn):
#     def wrapper(*args,**kwargs):
#         print("Decorator before calling function")
#         fn(*args,**kwargs)
#         print("Decorator after calling function")
#     return wrapper

class Human():
    #@my_deco
    def __init__(self):
        print("The initializer was called")

    def another_one(self):
        print("This is another method")
    
adam=Human() #object from a class
# adam.__init__()
#adam.__init__()
adam.another_one()
eve=Human()  # will call init but under eve
  

class Humanbeing():
    
    def __init__(self,gender,name):
        print("The initializer for Humanbeing was called")
        print(f"gender, {gender}")
        print(f"name, {name}")
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    def anotherone(self):
        print("This is another one from Humanbeing")

paul=Humanbeing(name="kamau", gender="male") #object from class
print("name",paul.name)
print("gender",paul.gender)
print("ribs",paul.ribs)
print("curse",paul.curse)
print("")


virginia=Humanbeing(name="wanja", gender="female") 
print("name",virginia.name)
print("gender",virginia.gender)
print("ribs",virginia.ribs)
print("curse",virginia.curse)

#learning about self 
class Learn():

    def __init__(self):
        print("The initializer for learn self was called")
        
        

    def learn_self(self,object,gender,name):
        object.gender=gender
        object.name=name
        if object.gender=="Male":
            object.ribs=24
            object.curse="Suffer"
        else :
          object.ribs=23
          object.curse="Pain"
    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")
    
# adam=Human(name="adam",gender="Male") #object from a class
# adam=Learn()
# adam.learn_self(name="adam",gender="Male",object=adam)
# print("name",adam.name)
# print("gender",adam.gender)
# print("ribs",adam.ribs)
# print("curse",adam.curse)
# print("")

adam=Learn()
adam.learn_self(name="adam",gender="Male",object=adam)
adam.print_self()

eve=Learn()
eve.learn_self(name="eve",gender="Female",object=eve)
eve.print_self()