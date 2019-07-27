# constructor: self calling function
''' 1. parametrized
    2. non parametrized
    no any return in constructor 
'''
class a:
    def __init__(self,name,id):  
        self.id = id 
        self.name = name  

    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  

emp1 = a("John",101)  
emp2 = a("David",102)  
  
#accessing display() method to print employee 1 information  
   
emp1.display();   
#a()

