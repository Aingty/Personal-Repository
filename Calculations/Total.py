import sys
import string

filename = "total.txt"

with open(filename) as f:
    content = f.readlines()

print("\n")
for line in content:
    line = line.split()
    if line[0] == "Name":
        continue
    if len(line) < 6:
        for i in range(1,len(line)):
            line[i] = float(line[i])
        total = line[1]+line[2]
        perCut = total * line[3]
        owe = line[4] + perCut
        line[4] = abs(line[4])
        if owe > 0:
            print("%s\nAM %.0f\nPM %.0f\n%.0f x %s = %.0f\n%.0f + %.0f = %.0f\n\nYou owe me %.0f"%(line[0],line[1],line[2],total,line[3],perCut,line[4],perCut,owe,owe))
        else:
            owe = abs(owe)
            print("%s\nAM %.0f\nPM %.0f\n%.0f x %s = %.0f\n%.0f - %.0f = %.0f\n\nI owe you %.0f"%(line[0],line[1],line[2],total,line[3],perCut,perCut,line[4],owe,owe))

    # else:
    #     line[4] = float(line[4])
    #     total = float(line[1])+float(line[2])
    #     perCut = float(total) * float(line[3])
    #     owe = line[4] + perCut
    #     line[4] = abs(line[4])
    print("\n-------------------------------------------------------------------------")