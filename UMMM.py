from random import choice
from time import sleep
print("this is an interactive simulation based on your choices.")

firstoption=input( "where would you like to be born: (1) United States (2)Germany (3) Japan (4)Italy (5)Russia (6)Cuba (7)United Kingdom : ")

if int(firstoption)==1 :
    print("You have chosen United States. One of the biggest world powers in history. ")
    sleep(1)
    print("...")
    sleep(2)
    secondoption= input("Which war will you participate in: (1) World War 1 (2)World War (3)Vietnam War ")
    sleep(1)
    print("...")
    sleep(1)
    if int(secondoption) == 1:
        print(" It's 1917 and the US decides to join in on World War 1 and you get drafted")
        sleep(1)
        print("..")
        sleep(1)
        print(" ")

