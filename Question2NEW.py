
supplied_pin = None
tries = 0

firstpin = input("PLEASE ENTER YOUR PIN NUMBER:")
if firstpin == "1234":
   tries += 1
   print("")
   print("PIN Attempts:", tries)
   exit("WELCOME")
else:
   tries +=1
   print("")
   print("PIN Attempts:", tries)

while supplied_pin != "1234":
   tries +=1
   if tries == 4 :exit("FAILED TO UNLOCK! -TOO MANY FAILED ATTEMPTS")
   print("INCORRECT PIN")
   supplied_pin = input("Enter Your Pin:")
   print("")
   print("PIN Attempts:", tries)
exit("WELCOME")
