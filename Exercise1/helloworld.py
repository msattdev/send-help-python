# Exercise:
# Write a program that, when run, greets the user by printing “Hello, world!” on the screen.
# Then it prints a message on the screen asking the user to enter their name. 
# The program greets the user by name by printing the “Hello,” followed by the user’s name.

print("Hello, world!")
print('What\'s your name?')
user_name = input() # Users name stored as variable user_name
print('Hello, ' + user_name + '.') # Using string concatenation, print hello user_name