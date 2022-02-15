import random# Gas Level Functiondef gasLevelGauge():


    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
   # print(currentGasLevel)
   return currentGasLevel

# Create If-ELIF-ELSE statements using comparative operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
        print("***WARNING***\n You have out of gas \n Calling Emergency contact")

gasLevelGauge()
gasLevelAlert()
