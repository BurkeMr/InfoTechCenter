
# WELCOME BRANCH 
# Codename Hornet
# https://realpython.com/python-sleep/#adding-a-python-sleep-call-with-timesleep

from time import sleep  # imports the sleep function from time


print("Welcome to Hornet's Info Tech Center!\n")
sleep(1)
print("Hornet's Operating System Booting Up!")

# GAS BRANCH

import random  # Gas Level Functiondef gasLevelGauge():


def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]

    currentGasLevel = random.choice(gasLevelList)

    # print(currentGasLevel)

    return currentGasLevel


# Varible calls the value of gasLevelGauge function

gasLevelIndicator = gasLevelGauge()


# Create If-ELIF-ELSE statements using the comparative operators == Equal to in order to display gas level messages

def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = random.randint(1,25)
    if gasLevelIndicator == "Empty":

        print("***WARNING YOU ARE ON EMPTY***\n You have ran out of gas \n Calling Emergency contact")

    elif gasLevelIndicator == "Low":

        print("      ***WARNING***\n You are almost out of gasoline\nThe closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away! ")

    elif gasLevelIndicator == "Quarter Tank":

        print("you are on a QUARTER TANK of gas\n  start planning a visit to the gas station!!! ")

    elif gasLevelIndicator == "Half Tank":

        print("you are on a HALF TANK of gas\n You have 125 more miles to empty  ")

    elif gasLevelIndicator == "Three Quarter Tank":

        print("you are on a THREE QUARTERS of gas\n You have 205 more miles to empty  ")

    else:

        print("you have a FULL TANK of gas, congratulations\n You have 310 more miles to empty  ")

    # Call Functions Here


# gasLevelGauge()

gasLevelAlert()

