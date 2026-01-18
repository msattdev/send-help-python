def printASCIITable():
    # Loop over integers 32 up to and including 126:
    for i in range(32, 127):
        # Print the integer and its ASCII text character:
        print(i, chr(i))

printASCIITable()