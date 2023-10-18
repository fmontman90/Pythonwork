
#First thing this shouyld do is check to make sure the text is 12 chars
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':# if fourth char in is not '-' return false
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":# if eighth char in is not '-' return false
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

#1st use of isPhoneNumber
print("Is 631-231-9454 a number: " + str(isPhoneNumber('631-231-9454')))
#print(isPhoneNumber('631-231-9454')) --> Thinking it is kinda optimized from what it was.
print("Is moosh a number: " + str(isPhoneNumber('moosh')))

#This goes to loop to see if text in message satifies
message = 'Hey, call me at 631-555-9987 today. 631-334-8888 is my office number'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('done')