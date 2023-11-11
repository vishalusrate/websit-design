print("Enter number one?")
num1 = int(input())
print("Enter pattern is asc - 1 or desc - 0")
num2 = input()
if num2 == '1':
    num2 = True
else:
    num2 = False 


for x in range(1,num1):
    if num2 == True:
        star = x * '*'
        print(star)
    elif num2 == False:
        star = (num1 - x) * '*'
        print(star)