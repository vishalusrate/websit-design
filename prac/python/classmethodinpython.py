class Employee:
   no_of_leave = 8
   def __init__(self,aname,agae,salary):
       self.name = aname
       self.age = agae
       self.salary = salary
		

   @classmethod
   def parse_dash_string(cls,string):
    # This is the one liner ....
    return cls(*string.split("-"))
       
    
    #    isko split karke maine class me pass kar diya hai .... isse wo dynamic ho jata hai 
    # parese_data = string.split("-")
    # return cls(parese_data[0],parese_data[1],parese_data[2])


karan = Employee.parse_dash_string("vishal-520-520")

print(karan.name)