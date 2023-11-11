# initializse the global varaible here 
global l
 # assigning the value to the global variable 
l=10

def function1(n):
    l =20 #this is the local variable scope .... ye wala variable aap khali isis function me use kar sakte hai 
    # ha isko change bhi kar sakte hai 
    l = 21
    # agar apko agar global ko change karna hai to ....  aap direct l =12 aise nahi kar sakte hai ye apko error de denga
    l = l + 21
    # agar apko global variable ko change karna hai to aap direct aise likh kar change kar sakte hai 
    # global l 
    # l = l+10
    print(l,"This is the print")


function1(12)


def function1():
    x=10
    def function2():
        # isko global function hi nahi mila to usne override nahi kiya aur local variacble ko hi print kiya niche ...
        global x
        x=20
    print("Before call function 2 ",x)
    function2()
    print("After call function 2 ",x)

function1()
# agar aap yaha par function ko run karte hai to apko 20 milenga to ye new variable bana kar usme ye wali value add kar denga
print("Out of the function ",x)