# By Kami Bigdely
# Split temp variable

def get_input(message):
    return input(message)

def save_into_db(info):
    print("saved into databse")

username = get_input('Please enter your username: ')
save_into_db(username)

birth_year = int(get_input('Please enter your birth year: '))
age = 2020 - birth_year

print("You are", age, "years old.")
