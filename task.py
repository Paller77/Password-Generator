import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', 'Ł', 'ß', '¤', '-', '_', 'đ', 'Đ']

print("Welcome to the PyWord password generator!")
number_of_letters = int(input(f"How many letters do you want in your PW?\n"))
number_of_numbers = int(input(f"How many numbers do you want in your PW?\n"))
number_of_symbols = int(input(f"How many symbols do you want in your PW?\n"))


PW_list = []

for i in range(number_of_letters):
    PW_list += random.choice(letters)

for j in range(number_of_numbers):
    PW_list += random.choice(numbers)

for k in range(number_of_symbols):
    PW_list += random.choice(symbols)


random.shuffle(PW_list)


password = ""
for char in PW_list:
    password += char

print(f"Your generated password is: {password}")




