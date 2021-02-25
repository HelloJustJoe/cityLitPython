# importing libraries/modules.
import random, string

# Builds each individual 12 character password
def generator():
    password = ""
    for _ in range(12):
        if random.randint(1,3) == 1:
            password += random.choice(string.digits)
        elif random.randint(1,3) == 2:
            password += random.choice(string.punctuation)
        else: 
            password += random.choice(string.ascii_letters)
    return password

# Calls generator function to build passwords 'num' amount of times.
def generate(num):
    for _ in range(num):
        print (generator())

# Prompt user for input
def userInput():
    return input("Would you like 10 more passwords? Y / N : ")

# Bringing the functions together. passwordGenerator invokes generate a 
# 'num' amount of times. 'num' is defaulted to 10 and is then passed to 
# the generate function. Once passed the user is prompted for input, if 
# user selects anything other than 'y' the script will exit.
def passwordGenerator(num = 10):
    generate(num)
    choice = userInput()
    while choice == "y":
        generate(num)
        choice = userInput()

# calling password generator.
passwordGenerator()