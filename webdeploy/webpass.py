import random 
import string
import sys

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

all = lower + upper + num  

temp = random.sample(all,10)

password = "".join(temp)
sys.stdout = open('webserverpass', 'w')
print(password)
sys.stdout.close()
