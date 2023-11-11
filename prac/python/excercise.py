

def getdate():
    import datetime
    return datetime.datetime.now()


def user_input_lock():
    print("Enter the name of the user")
    name_user = input()
    print("Enter the 1 for food and 2 for the excercise ")
    activity = int(input())

    if(activity == 1):
        print("Enter the which food do you eat?")
        food = input()
        date = getdate()
        f = open(name_user+"food.txt","a")
        f.write('['+str(date)+'] '+ food + '\n')
    elif activity == 2:
        print("Enter the which Exercise doing?")
        excercise = input()
        date = getdate()
        f = open(name_user+"excercise.txt","a")
        f.write('['+str(date)+'] '+excercise + '\n')

def see_user_details():
    print("Enter the name of the user")
    name_of_the_user = input()
    print("Enter 1 for food and 2 for excercise")
    activity_check = int(input())
    if  activity_check == 1:
        with open(name_of_the_user+'food.txt') as f:
            print(f.readlines())
    else:
        with open(name_of_the_user+'excercise.txt') as f:
            print(f.readlines())
    
while(True):
    print("Pease enter 1 for lock the information and 2 for see the details of the user")
    user_input = int(input())
    if user_input == 1:
        user_input_lock()
    else: 
        see_user_details()





