import random
import string

password_length = random.randint(8, 15)
characters = string.ascii_letters + string.digits
# string.digits for 0123456789 digits and string.ascii_letters all in the form of string
password = "".join([random.choice(characters) for i in range(password_length)])
print(password)
