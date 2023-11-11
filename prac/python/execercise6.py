import random
items = ['g','s','w']
run_cont = 1
tie = 0
c=0
u=0
computer = []
user = []
while(True):
  
    if run_cont > 10:
        break

    print("Please enter s-snake , w- water, g- gun")
    un_input = input()
    c_input = random.choice(items)
    if(un_input == c_input):
        tie +=1
        run_cont =  run_cont +1
    elif(un_input == 's' and c_input == 'w'):
        u +=1
        user.append(un_input)
        computer.append(c_input)
        run_cont =  run_cont +1
    elif(un_input=='g' and c_input == 's'):
        u +=1
        user.append(un_input)
        computer.append(c_input)
        run_cont =  run_cont +1
    elif(un_input == 'w' and c_input == 'g'):
        u +=1
        user.append(un_input)
        computer.append(c_input)
        run_cont =  run_cont +1
    elif(c_input == 's' and un_input == 'w'):
        c +=1
        computer.append(c_input)
        user.append(un_input)
        run_cont =  run_cont +1
    elif(c_input == 'w' and un_input == 'g'):
        c +=1
        computer.append(c_input)
        user.append(un_input)
        run_cont =  run_cont +1
    elif(c_input == 'g' and un_input == 's'):
        c +=1
        computer.append(c_input)
        user.append(un_input)
        run_cont =  run_cont +1
if(c>u):
    print("Computer is win:- ",c )
    print("Computer items :- ",computer)
    print("User items :- ",user)
elif(u>c):
    print("user is win :- ",u)
    print("Computer items :- ",computer)
    print("User items :- ",user)



