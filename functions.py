# A collection of instruction
#
#Def for define
def fucntion1():
    print("inside the func")#part of func
    print("inside the func2")#part of func
print("outside the function")
fucntion1() # The call of ther function
""" what the code was
def sometext(mess):
  
    mess = input("Please enter go, stop, or pause:")

    if mess != "stop":
        print("This loop will keep on going!")
        
    else:
        print("Guess it stopped!")

text =""

sometext(text) """
def someText(mess):
#Now what it is
    mess = input("Please enter go, stop, or pause:")
    # while not equal to stop input, keep on going
    while mess != "stop":
        print("This loop will keep on going! Maybe try stop?")
        mess = input("Please enter go, stop, or pause:")
    else:
        print("Guess it stopped!")

text =""
someText(text)