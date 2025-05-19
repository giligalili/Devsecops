import random

letters = list("string.ascii_lowercase+string.ascii_uppercase")  # Convert the string into a list
shuffled_letters = letters[:]  # Make a copy to shuffle
random.shuffle(shuffled_letters)  # Shuffle the copied list

d = dict(zip(letters, shuffled_letters))  # Create the dictionary

print(d)
