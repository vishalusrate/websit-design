name = "vishal"
age = 23

# this is the one way to declare the variable in the python
# a = "This is the %s %s"% (name ,age)

# this is another way to bind the variable in the given string
# a = "This is {} {}"
# c = a.format(name,age)

# isme readablity kam hoti hai aur program me agar jada variable hue to manage karna hard hota hai 
f_string = f"This is the {name } and My age is :- {age }"
print(f_string)