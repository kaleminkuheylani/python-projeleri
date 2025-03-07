from random import randint

def random_password_generator():
    password = ""
    for i in range(10):  # 10 characters for the password
        random_number = randint(33, 126)  # Use ASCII printable characters
        random_char = chr(random_number)
        password += random_char
    return password

def password_solver(passw):
    real_password = ""
    for i in range(len(passw)):
        while True:
            random_number = randint(33, 126)  # Generate printable ASCII characters
            random_char = chr(random_number)
            if passw[i] == random_char:
                real_password += random_char
                break  # Exit the loop once the correct character is found
    return real_password

# Test the functions
generated_password = random_password_generator()
print("Generated Password:", generated_password)
print("Solved Password:", password_solver(generated_password))

