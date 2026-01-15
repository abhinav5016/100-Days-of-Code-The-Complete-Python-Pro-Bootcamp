import random

letters = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]


symbols = [
    "!","@","#","$","%","^","&","*",
    "-","_","+","=","?",".",",","/"
]


print("Welcome to Password Generator")

no_letters = int(input("How many letters need in your password.\n"))
no_symbol = int(input("How many symbol need in your password.\n")) 
no_numbers = int(input("How many numbers need in your password.\n")) 

password = []

for char in range(0, no_letters):
    password.append(random.choice(letters))

for char in range(0, no_symbol):
    password.append(random.choice(symbols))    
    
for char in range(0, no_numbers):
    password.append(random.choice(numbers))  

random.shuffle(password)
 

final_password = ""
for char in password:
    final_password += char

print(f"Your password is: {final_password}")





