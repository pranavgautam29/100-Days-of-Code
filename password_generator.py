import random
print("Welcome to Password Generator")
letters = int(input("How many letters would you like in your password:"))
n = int(input("How many numbers would you like in your password:"))
symb = int(input("How many symbols would you like in your password:"))
password_list = []
password = ""
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
     'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
     '*', '(', ')', '<']
for i in range(1, letters+1):

    password_list += random.choice(l)

for j in range(0, n):

    password_list += random.choice(num)

for t in range(0, symb):

    password_list += random.choice(s)

for p in range(0, len(password_list)):
    password += random.choice(password_list)
print("Your password is:", password)

