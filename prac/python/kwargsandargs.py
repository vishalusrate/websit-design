
# isse aap limites parameter bhej sakte ho 
def funtion_get_user_data(a,b,c,d,r,f):
    print(a,b,c,d,r,f)

# limited parameter bhej sakte ho .... 
# funtion_get_user_data("vishal","lakhan","dada","test","abc","bcd")


# agar apko dynamic parameter bhejne hai kisi bhi function me aur wo kitne hai apko pata nahi hai .... to aap kwargs and args use kar sakte hai

def funct(text,*args):
    # args tuple ti tarah isme atta hai 
    print(text)
    for item in args:
        print(item)

    # print(args)

# aap isme list aur tuple dono pass kar sakte hai aur aap dusra variable bhi pass kar sakte ho but sabse first me pass karna padenga .... nahi to error aa jayenga

list_name = ["vishal","lakhan","dada","test","abc","bcd"]
text = "This is the first element in the args and kwargs other wise it's show error"
# funct(text , *list_name)



# if you pass like this then it's show the error 
def funct1(*args,text):
    print(text)
    for item in args:
        print(item)

# funct1(*list_name,text)

#aise error atta hai agar apko aise error ko nahi chaiye to aap isme parameter barabar pass karo .... sabse pahile apko normal arg ment dene ahi aur uske bad apko args and kwargs dene hai ....
#     
# Traceback (most recent call last):
#   File "c:\Users\ukv-208\Downloads\prac\python\kwargsandargs.py", line 34, in <module>
#     funct1(*list_name,text)
# TypeError: funct1() missing 1 required keyword-only argument: 'text'


# Solution Of the error :- 
def funct2(text,*argsparam,**kwargsparam):
    print(text)
    for item in argsparam:
        print(item)
    print("This is the kwargs section")
    for key,value in kwargsparam.items():
        print(f"{key} of the and value is {value}")


#  funct2(text,*list_name)

#  File "c:\Users\ukv-208\Downloads\prac\python\kwargsandargs.py", line 56
#     name_of_employee = ['name':'vishal','age':'18',"City":'aurangabad']
#                               ^
# SyntaxError: invalid syntax
# solution :-
# you not pass the in the list key and value paisr use the dictionary instead of the list

name_of_employee = {'name':'vishal','age':'18',"City":'aurangabad'}
# isi tarah aap isme kwargs bhi pass kar sakte hai 
funct2(text,*list_name,**name_of_employee)
