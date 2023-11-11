lis = ["1","2","3","4","5","5"]

# sabse pahile maine int me convert kiya hai isko uske baad usko hamne add kiya hai .... but same kaam haam map function se kar sakte hai 
lis = list(map(int,lis))

# for i in range(len(lis)):
#     lis[i] = int(lis[i])


# agar apko squre nikalne hai kisis list ke item ke to aap usko nikal sakte ho 

lis_num = [1,2,2,4,5,6,7,8,9,0,0,77,7,5]
square_using_lambda = list(map(lambda x : x*x,lis_num))
# dusra hota hai ki aap function banakar use kar sakte hai 

def squr(x):
    return x*x

# isse aap function call karke nikal sakte ho 
# print(list(map(squr,lis_num)))

def sq(x):
    return x*x

def cube(x):
    return x*x*x

lis_number = [sq,cube]

for i in range(5):
    val = list(map(lambda x:x(i),lis_number))
    # print(val)


# filter function in the python

li = [1,2,3,4,5,6,7,8,9,0,56]
def num_greter_than_2(x):
    return x>2

f = list(filter(num_greter_than_2,li))

# print(f)

import functools as t
list3 = [1,2,3,4,5]
# agar apko iske total sub dekhni hogi to aap isko loop me chala kar add karenge

# num = 0
# for i in list3:
#     num = num+i
# but iske alava bhi iski sum kar sakte hai 

num = t.reduce(lambda x,y:x*y,list3)
print(num)

