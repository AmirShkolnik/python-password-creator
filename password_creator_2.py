import random
import string
print("Welcome to the Password Generator!")
length = int(input(f"Choose the length of your password: \n"))
characters = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
password = ''.join(random.choice(characters) for _ in range(length))
print("Your random password is:", password)