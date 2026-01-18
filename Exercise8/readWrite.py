# def writeToFile(filename, text):
#     # Open the file in write mode:
#     with open(filename, ____) as fileObj:
#         # Write the text to the file:
#         ____.write(text)
 
# def appendToFile(filename, text):
#     # Open the file in append mode:
#     ____ open(filename, ____) as fileObj:
#         # Write the text to the end of the file:
#         ____.write(____)
 
# def readFromFile(filename):
#     # Open the file in read mode:
#     ____ ____(filename) as fileObj:
#         # Read all of the text in the file and return it as a string:
#         return ____.read()

def writeToFile(filename, text):
    with open(filename, mode='w') as file:
        file.write(text)

def appendToFile(filename, text):
    with open(filename, mode='a') as file:
        file.write(text)

def readFromFile(filename):
    with open(filename) as file:
        return file.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'