name = input("Enter your name:")

#Try to convert string into an int number
#Except prints error if input cannot be converted into int number
try:
    x = int(name)
    print(x)
except:
    print("ERROR: Input is not a int number!")


