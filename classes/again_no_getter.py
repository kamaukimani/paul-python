

class Rectangle():

    def __init__(self,length,width):
        
        #length and width hhave to be a number
        if not isinstance(length,(int,float)):
            raise TypeError(f"Exptected a number, got {type(length)}")
        
        if not isinstance(width,(int,float)):
            raise TypeError(f"Exptected a number, got {type(width)}")
        
        self.length=length
        self.width=width
        
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return (2*self.length)+(2*self.width)
    
    def info(self):
        print("-------------------------")
        print("Shape is rectange")
        print("Length is",self.length)
        print("Width",self.width)
        print("Area",self.area())
        print("Perimeter",self.perimeter())
        print("-------------------------")

r1=Rectangle(length=30,width=12)
        
r1.info()

#r1.length="hello world"
#r1.info()
