import time, csv, os
sFolder = r'c:/dumps/'
startTime = time.clock()
tAlarmPriority = [18,21,24,27,30,33,37]
for x in os.listdir(sFolder):
    fileArr = sFolder + x
    with open(fileArr, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        stdOut = ''
        for row in reader:
            if row[0][0] == ':':
                for item in row[:-1]:
                    stdOut += item + ','
                if row[0][0:6] == ':mode=':
                    stdOut += ':mode=replace\n'
                else:
                    stdOut += row[len(row)-1] + '\n'
            if row[0][0] == ':' or row[0][0:6] == ':mode=':
                sRowType = row[0]
                if row[0][0:6] == ':mode=':
                    sRowType = row[0][0:6]
            if sRowType == ':mode=' and row[0][0] != ':':
                pass
            if sRowType == ':IOAccess' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s\n' % tuple(row)
            if sRowType == ':AlarmGroup' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':MemoryDisc' and row[0][0] != ':':
                if row[10] != 'None' and float(row[11]) <= 3:
                    # if float(row[11]) >= 3:
                    #     print(row[0], float(row[11]))
                    pass#stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
            if sRowType == ':IODisc' and row[0][0] != ':':
                if row[10] != 'None' and float(row[11]) <= 3:
                    #if float(row[11]) >= 3:
                    #    print(row[0], float(row[11]))
                    pass#stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,"%s","%s"\n' % tuple(row)
            if sRowType == ':MemoryInt' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    for i in tAlarmPriority:
                            row[i] = 3
                    stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':IOInt' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    for i in tAlarmPriority:
                            row[i] = 3
                    stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':MemoryReal' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    for i in tAlarmPriority:
                            row[i] = 3
                    stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':IOReal' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    for i in tAlarmPriority:
                            row[i] = 3
                    stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':MemoryMsg' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s"\n' % tuple(row)
            if sRowType == ':IOMsg' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s"\n' % tuple(row)
            if sRowType == ':GroupVar' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':HistoryTrend' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':TagID' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s","%s"\n' % tuple(row)
            if sRowType == ':IndirectDisc' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row)
            if sRowType == ':IndirectAnalog' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row)
            if sRowType == ':IndirectMsg' and row[0][0] != ':':
                pass
                #stdOut += '"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row)
    with open('c:/mods/' + x, 'w') as file:
        file.write(stdOut)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")