def factoria_using_iteration(n):
    """
        factorial using iteration process 
    """
    fact = 1
    for i in range(n):
       fact = fact * (n-i)

    print("Factorial is the given number is:- ", fact)
    # return fact


def factorial_using_recrusion(n):
    if n==1:
        return 1
    else:
       return n * factorial_using_recrusion(n-1)
    

def fibnossi_number(n):
    if n ==1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibnossi_number(n-1) + fibnossi_number(n-1)

# factoria_using_iteration(5)
# result = factorial_using_recrusion(5)
# print("Factorial is the given number is:- ",result)
result = fibnossi_number(5)
print("Fibnossi  number is:- ",result)