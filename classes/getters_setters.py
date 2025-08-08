
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

#how to create a class <-->What a class is
# initialiZer <constrocture>
# self key what it is :<this>

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       

class Human():

    def __init__(self,gender,name):
        print("The initializer wass called")
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    @property
    def get_name(self):
        print("Somebody wants to get the name of a property")
        write_file(f_name="log.txt",txt=f"Tried to get name ")
        return self.name
    
    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")


# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
# adam.name
# adam.print_self()
print(adam.get_name)
print(adam.name) # he will
#expilicity calling the get_name
# Gett data from an object

# getting data or reading data

# Getters and Setters
#----> Security<python> ---> Like Decorator -->modify when tries to get
# Control how thhe data is gotten.

# employee-> salary -> modified when its being modified