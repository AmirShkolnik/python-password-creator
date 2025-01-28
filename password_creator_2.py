import random
import string

length = int(input(f"Choose the length of your passwor: \n"))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Your random password is:", password)