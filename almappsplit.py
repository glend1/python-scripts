import time, csv
startTime = time.clock()
stdSmeltingOut = ''
stdChemicalsOut = ''
tAccessNameList = []
iAccessNamePos = 0
line = 0
printCheck = False
tSmelting = ['PLC1', 'PLC2', 'PLC3', 'PLC4', 'PLC5', 'PLC6', 'PLC9', 'PLC19', 'PLC20', 'PLC27', 'PLC29']
tChemicals = ['enercon', 'iobox', 'iobox2', 'iobox3', 'iobox4', 'PLC7', 'PLC8', 'PLC10', 'PLC11', 'PLC12', 'PLC13', 'PLC14', 'PLC16', 'PLC17', 'PLC18', 'PLC21', 'PLC22', 'PLC23', 'PLC25', 'PLC26', 'PLC28']
def fPlcCheck(sName, tList):
    for sPlc in tList:
        if sPlc == sName:
            return True 
with open('c:/newalarms.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        printCheck = False
        line += 1
        if row[0][0] == ':':
            i = 0
            header = row[0]
            for item in row[:-1]:
                stdSmeltingOut += item + ','
                stdChemicalsOut += item + ','
                if item == 'AccessName' or item == 'Topic':
                    tAccessNameList.append([row[0], i])
                i += 1
            if row[0][0:6] == ':mode=':
                stdSmeltingOut += ':mode=replace\n'
                stdChemicalsOut += ':mode=replace\n'
            else:
                stdSmeltingOut += row[len(row)-1] + '\n'
                stdChemicalsOut += row[len(row)-1] + '\n'
            continue
        for accessList in tAccessNameList:
            if accessList[0] == header:
                iAccessNamePos = accessList[1]
                if row[iAccessNamePos] == 'PLC166':
                    row[iAccessNamePos] = 'PLC29'
                if fPlcCheck(row[iAccessNamePos], tSmelting) == True:
                    if header == ':IODisc':
                        stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
                    if header == ':IOInt' or header == ':IOReal':
                        stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                    if header == ':IOMsg':
                        stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s"\n' % tuple(row)
                    if header == ':IOAccess':
                        if row[2] == 'enercon' or row[2] == 'iobox' or row[2] == 'iobox2' or row[2] == 'iobox3' or row[2] == 'iobox4':
                            row[1] = '\\\\ts2\\multi485'
                        else:
                            row[1] = 'server_runtime'
                        stdSmeltingOut += '"%s","%s","%s",%s,%s\n' % tuple(row)
                elif fPlcCheck(row[iAccessNamePos], tChemicals) == True:
                    if header == ':IODisc':
                        stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
                    if header == ':IOInt' or header == ':IOReal':
                        stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                    if header == ':IOMsg':
                        stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s"\n' % tuple(row)
                    if header == ':IOAccess':
                        if row[2] == 'enercon' or row[2] == 'iobox' or row[2] == 'iobox2' or row[2] == 'iobox3' or row[2] == 'iobox4':
                            row[1] = '\\\\ts2\\multi485'
                        else:
                            row[1] = 'server_runtime'
                        stdChemicalsOut += '"%s","%s","%s",%s,%s\n' % tuple(row)
                else:
                    print(line, row[iAccessNamePos], row[0])
                printCheck = True
        if printCheck == False:
            if header == ':AlarmGroup':
                stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                printCheck = True
            if header == ':MemoryDisc':
                stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
                printCheck = True
            if header == ':MemoryInt' or header == ':MemoryReal':
                stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
                printCheck = True
            if header == ':MemoryMsg':
                stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s"\n' % tuple(row)
                printCheck = True
            if header == ':GroupVar' or header == ':HistoryTrend' or header == ':TagID':
                stdSmeltingOut += '"%s","%s","%s","%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s","%s"\n' % tuple(row)
                printCheck = True
            if header == ':IndirectDisc' or header == ':IndirectAnalog' or header == ':IndirectMsg':
                stdSmeltingOut += '"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row)
                stdChemicalsOut += '"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row)
                printCheck = True
        if printCheck == False:
            print(line, row)
with open('c:/chemicals.csv', 'w') as file:
    file.write(stdChemicalsOut)
with open('c:/smelting.csv', 'w') as file:
    file.write(stdSmeltingOut)
print(tAccessNameList)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")

