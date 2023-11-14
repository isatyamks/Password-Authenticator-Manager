import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
  
    characters = characters.replace(" ", "p")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

loop=int(input("Enter the Quantity:"))

temp_loop=loop

print("Generated Password:")
while(loop):
    generated_password = generate_password(12)
    print(temp_loop - loop + 1, "--->>  ", generated_password, "\n")
    loop=loop-1



