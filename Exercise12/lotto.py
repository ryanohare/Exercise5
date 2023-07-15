import random

def generate_random_numbers():
    random_numbers = []
    for _ in range(6):
        random_numbers.append(random.randint(1, 50))
    return random_numbers

# Generate a list of 6 random numbers between 1 and 50
random_number_list = generate_random_numbers()

# Print the random numbers
print(random_number_list)
