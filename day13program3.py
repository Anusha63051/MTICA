def printSunday():
    print('sunday')
    return
def printMonday():
    print('monday')
def printTuesday():
    print('tuesday')
def printWednesday():
    print('wednesday')
def printThursday():
    print('thursday')
def printFriday():
    print('friday')
def printSaturday():
    print('saturday')
def choice():
    print("Enter day number between 1-7")
    return
dayDict={0:printSunday,1:printMonday,2:printTuesday,3:printWednesday,4:printThursday,5:printFriday,6:printSaturday}

choice()
dayNo=int(input())
if dayNo>=0 and dayNo<=6:
    dayDict[dayNo]()
else:
    print("INVALID")
