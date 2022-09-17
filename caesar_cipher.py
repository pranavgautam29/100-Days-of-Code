print("Welcome to Caesar Cipher")
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def caeser(command , plain_text , number_shift):
    if command == 'encode':
            out = ""
            for letter in plain_text:
                if letter in alphabets:
                    position = alphabets.index(letter) + number_shift
                    out += alphabets[position]
                else:
                    out += letter
            print("Encoded message:",out)
    elif command == 'decode':
        dec = ""
        for letter in plain_text:
            if letter in alphabets:
                pos = alphabets.index(letter) - number_shift
                dec += alphabets[pos]
            else:
                dec += letter
        print("Decoded message:",dec)
    else:
        print("Invalid Input")
should_continue = True
while should_continue:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt , 'decode' to decrypt:")
    text = input("Type the message:").lower()
    shift = int(input("Type the shift number:"))
    shift = shift%26
    caeser(command = direction , plain_text=text , number_shift=shift)
    result = input("Type 'yes' to cipher again or 'no' to exit:").lower()
    if result == "no":
        print("GoodBye")
        should_continue = False