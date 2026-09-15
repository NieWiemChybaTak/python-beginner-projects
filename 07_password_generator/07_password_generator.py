import string
import random

print("== Welcome to the password generator. ==")

def get_length(no_chars):
    while True: 
        try:
            chars_num = int(input(no_chars))
            if chars_num >=4:
                return chars_num
            else:
                print("Password too short")
        except ValueError:
                print("Password length must be a number")

pass_length = get_length("How many characters do you want your password to have? Give number (min 4) ")
def get_characters(question, characters):
            while True:
                q_answer = input(question).lower()
                if q_answer == "y":
                    return characters
                elif q_answer == "n":
                    return  ""
                else:
                    print("Only y or n")

lc_letters = get_characters("Should password contain lowercase letters? y/n ", string.ascii_lowercase)
uc_letters = get_characters("Should password contain uppercase letters? y/n ", string.ascii_uppercase)
dig_pass = get_characters("Should password contain digits? y/n ", string.digits)
spc_pass = get_characters("Should password contain special characters? y/n ", string.punctuation)    

ltrs = (lc_letters)+(uc_letters)+(dig_pass)+(spc_pass)

def create_pswrd(length, letters):
    password = ""
    while len(password)< length:
         password += random.choice(letters)
    return password
 
if len(ltrs)>0:
    password = create_pswrd(pass_length, ltrs)
    print(password)
else:
    print("No characters picked, password not generated")
