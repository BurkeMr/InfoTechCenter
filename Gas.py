import random# Gas Level Functiondef gasLevelGauge():

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full"]
    currentGasLevel = random.choice(gasLevelList)
    # print(currentGasLevel)
    return currentGasLevel

# Create If-ELIF-ELSE statements using comparative operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty":
        print("***WARNING***\n You have ran out of gas \n Calling Emergency contact")
    elif gasLevelGauge() == "Low":
        print("      ***WARNING***\n You are almost out of gasoline\nThe closest gasoline station is ")

#gasLevelGauge()
gasLevelAlert()
