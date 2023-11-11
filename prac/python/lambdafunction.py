# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Lambda and annomus function using python")

# this is the function where you can add the two number but same work you do using the lambda function and lamda function is also knowon as the annomus function 

# def sum_of_the_number(a,b):
#     return a+b
   
# lamda bhi ek tarah ka function hota hai wo same function ki tarah kaam karta hai ..... usme aap function ki tarah hi kuch kaam kar sakte hai 

# sum_of_the_number = lambda x,b : x+b

# sum = sum_of_the_number(3,2)
# print("Sum of the 2 number is :- ",sum)

def return_first_number_of_the_number(n):
    return n[1]

list_number = [[1,23],[5,10],[0,2],[5,80]]

# ye wala function call karke kiya but same chizse haam lambda use karke kar sakte hai 

# list_number.sort(key=return_first_number_of_the_number)

list_number.sort(key = lambda x : x[1])

print(list_number)