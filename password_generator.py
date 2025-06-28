import random, string

try:
    length = int(input("Password length: "))
    if length > 0:
        chars = string.ascii_letters + string.digits + string.punctuation
        print("Your password:", ''.join(random.choices(chars, k=length)))
    else:
        print("Length must be greater than 0.")
except:
    print("Enter a valid number.")
