import time, csv
startTime = time.clock()
iLine = 0
tOut = []
stdOut = ''
tSmelting = ['PLC1', 'PLC3', 'PLC4', 'PLC5', 'PLC6', 'PLC9', 'PLC19', 'PLC20', 'PLC27', 'PLC29']
tChemicals = ['PLC7', 'PLC8', 'PLC10', 'PLC11', 'PLC12', 'PLC14', 'PLC16', 'PLC17', 'PLC18']
def fPlcCheck(sName, tList):
    for sPlc in tList:
        if sPlc == sName:
            return True
with open('c:/insql2dump.txt', 'r') as file:
    reader = csv.reader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in reader:
        iLine += 1
        if row[0][0] == ':': 
            sHeader = row[0]
        if sHeader == ':(IODriver)ComputerName':
            pass
        if sHeader == ':(IOServer)ComputerName':
            pass
        if sHeader == ':(Topic)Name':
            pass
        if sHeader == ':(AnalogTag)TagName' or sHeader == ':(DiscreteTag)TagName' or sHeader == ':(StringTag)TagName':
            if row[0][0] != ':':
                if fPlcCheck(row[4], tSmelting) == True:
                    row[2] = 'TS4'
                if fPlcCheck(row[4], tChemicals) == True:
                    row[2] = 'TS2'
        tOut.append(row)
for line in tOut:
    for element in line:
        stdOut += element + '\t'
    stdOut += '\n'
with open('c:/output.txt', 'w') as file:
    file.write(stdOut)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")