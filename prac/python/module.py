import random

# platform modules gives you main dir and path name 
import platform
import statistics

rand = random.randint(0,3)

rand = random.random() * 100

lit = ['vishal','kaka','mama','dada','test','gfddfdf']
print(random.choice(lit))

# gives directory name of the current file 

dir_name = dir(platform)
print(dir_name)

# gives processsor information 
print(platform.processor())


import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)


url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)