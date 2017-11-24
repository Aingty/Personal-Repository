import sys
import string

filename = "cal.txt"

total = 0
lineNum = 0
with open(filename) as f:
    content = f.readlines()

print("\n")   
for line in content:
    lineNum += 1
    numTest = 0
    expectMoney = False
    moneyRecieved = False
    isTwoDigit = False
    tempMoney =""
    for char in line:
        if char.isdigit() and expectMoney == False:
            numTest += 1
            if numTest == 3:
                expectMoney = True
                numTest += 1
                next
        elif expectMoney == False and numTest == 2:
            expectMoney = True
            isTwoDigit = True
            numTest += 1
            next
        else: 
            if char.isdigit() and expectMoney == True:
                if numTest == 4 and isTwoDigit == False:
                    print("Error with a fourth digit number at line ", lineNum)
                    sys.exit()
                else:
                    moneyRecieved = True
                    tempMoney += char
            else:
                numTest += 1 #Increment numTest by 1 so it is not a 4 for isdigit test
                if moneyRecieved:
                    if ' ' in tempMoney:
                        tempMoney = ""
                        next
                    else:
                        #print(tempMoney)
                        total = total + int(tempMoney)
                        tempMoney = ""
                    # if char.isspace():
                    #     numTest = 0
                    #     expectMoney = False
                    #     moneyRecieved = False
print("\nThe total is ", total)
