import time, csv, os
sFolder = r'c:/tbrc.csv'
startTime = time.clock()
word = ['PLC166']
def fPlcFilter(match):
    for x in word:
        if x == match:
            return True
for x in os.listdir(sFolder):
    fileArr = sFolder + x
    with open(fileArr, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        stdOut = ''
        for row in reader:
            if row[0][0] == ':' or row[0][0:6] == ':mode=':
                sRowType = row[0]
                if row[0][0:6] == ':mode=':
                    sRowType = row[0][0:6]
            if sRowType == ':MemoryDisc':
                if row[0][0] == ':' or row[10] == 'On':
                    stdOut += '%s,%s,"%s",%s,%s,"%s"\n' % (row[0], row[1], row[2], row[10], row[11], row[12])
            if sRowType == ':IODisc':
                if fPlcFilter(row[13]) == True:
                    if row[0][0] == ':' or row[10] != 'None':
                        stdOut += '%s,%s,"%s",%s,%s,%s,%s\n' % (row[0], row[1], row[2], row[10], row[11], row[13], row[15])
            if sRowType == ':IOInt':
                if fPlcFilter(row[42]) == True:
                    if row[0][0] == ':' or row[16] == 'On' or row[19] == 'On' or row[22] == 'On' or row[25] == 'On' or row[28] == 'On'  or row[31] == 'On' or row[35] == 'On':
                        stdOut += '%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s"\n' % (row[0], row[1], row[2], row[16], row[18], row[19], row[21], row[22], row[24], row[25], row[27], row[28], row[30], row[31], row[32], row[42], row[44], row[46])
            if sRowType == ':IOReal':
                if fPlcFilter(row[42]) == True:
                    if row[0][0] == ':' or row[16] == 'On' or row[19] == 'On' or row[22] == 'On' or row[25] == 'On' or row[28] == 'On' or row[31] == 'On'  or row[35] == 'On':
                        stdOut += '%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s"\n' % (row[0], row[1], row[2], row[16], row[18], row[19], row[21], row[22], row[24], row[25], row[27], row[28], row[30], row[31], row[32], row[42], row[44], row[46])
    with open('c:/mods/' + x, 'w') as file:
        file.write(stdOut)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")