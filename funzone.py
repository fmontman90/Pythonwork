#This is meant to test code

mess = input("Please enter go, stop, or pause:")

while mess != "stop":
    print("This loop will keep on going!")
    mess = input("Please enter go, stop, or pause:")
else:
    print("Guess it stopped!")