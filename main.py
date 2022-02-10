
from os import system, name
from time import sleep
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
while True: 
sleep(2)
clear()

while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        
        continue
    else:
        break
if age >= 100: 
    print("please enter a valid age")
    
elif age in range (17, 100):
    print("you can vote in the United States")

else:
    print("You are not able to vote in the United States.")
 
        
