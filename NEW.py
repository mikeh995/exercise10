attempts = 2
authenticated = False
correctPin = "1234"


def ValidatePin(pin):
    if pin == correctPin:
        return True
    else:
        return False


while attempts >= 0 and authenticated == False:
    currentPin = input("Please enter your pin")

    isValid = ValidatePin(currentPin)

    if isValid == True:
        authenticated = True;
        print("You have been authenticated")
    else:
        attempts = attempts - 1
        print("incorrect pin")

if attempts < 0:
    print("Your account has been locked")
else:
    print("Your balance is 1 million ugandan dollars")
