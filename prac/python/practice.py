
def funct1(num):
    if num == 0:
        return print
    else:
        return sum
    
test3 = funct1(1)
del funct1
# ye delete karne bad bhi run hoga kyu ki maine uski copy bana li hai ek variable me ... but aap funct1 ko use nahi kar sakte hai 
print(test3)

print(funct1(0))


def test(funct):
    def test1():
        print("Test one executed")
        funct()
        print("After executed")
    return test1()
# aap aise bhi decoraters ko call kar sakte hai .... decoraters se aap multiple function initilizse karke use kar sakte hai ....jaab apko 3 se 4 function ek hi time pe call karne hote hai taab 

@test
def ma():
    print("Who is vishal")

# aap aise bhi decoraters ko call kar sakte hai aur @test aise ma function ke upper likh kar bhi kar sakte hai 

# who_is_vishal = test(ma)
print(ma)


