import time, csv, os, re
sFolder = r'c:/dumps/'
startTime = time.clock()
tSystemGroup = ['', '', '', 'Yes', '999', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '']
stdOut = ''
errorDump = ''
tTagnamesFiles = [] 
tGroupNamesFiles = []
tTagnamesFilesDuplicate = []
tGroupNamesFilesDuplicate = [] 
tIOAccess = []
tAccessNames = []
tIOAccessCorrected = []
tAlarmGroupCorrect = [] 
tMemoryDisc = [] 
tIODisc = []
tMemoryInt = [] 
tIOInt = []
tMemoryReal = [] 
tIOReal = []
tIOMsg = []
tMemoryMsg = [] 
tIOMsg = []
tGroupVar = []
tHistoryTrend = [] 
tTagID = []
tIndirectDisc = []
tIndirectAnalog = [] 
tIndirectMsg = []
def fDuplicateTest(inputList, output):
    for firstFilenameTagname in inputList:
        for firstName in firstFilenameTagname[1]:
            for secondFilenameTagname in inputList:
                if firstFilenameTagname[0] == secondFilenameTagname[0]:
                    break
                else:
                    for secondName in secondFilenameTagname[1]:
                        if firstName == secondName and firstName != '$System':
                            output.append([firstFilenameTagname[0], secondFilenameTagname[0], secondName])
def fDuplicateCheck(duplicateList, firstName):
    bDuplicateName = False
    if len(duplicateList) == False:
        duplicateList.append(firstName)
    for secondName in duplicateList:
        if firstName == secondName:
            bDuplicateName = True
            break
    if bDuplicateName == False:
        duplicateList.append(firstName)     
for filename in os.listdir(sFolder):
    fileArr = sFolder + filename
    with open(fileArr, 'r') as file:
        rFilename = re.search('^.+([\.])', filename)
        sFilename = rFilename.group(0)[:-1].title()
        sFilenameSafe = sFilename.replace(' ', '_')
        reader = csv.reader(file, delimiter=',')
        tTableHeaders = []
        tGroupNames = []
        tTagnamesFile = []
        tAlarmGroup = []
        bSystemGroup = False
        for row in reader:
            if row[0][0] == ':':
                sTableHeader = ''
                for item in row[:-1]:
                    sTableHeader += item + ','
                if row[0][0:6] == ':mode=':
                    sTableHeader += ':mode=replace\n'
                else:
                    sTableHeader += row[len(row)-1] + '\n'
                tTableHeaders.append(sTableHeader)
            if row[0][0] == ':' or row[0][0:6] == ':mode=':
                sRowType = row[0]
                if row[0][0:6] == ':mode=':
                    sRowType = row[0][0:6]
            if sRowType == ':mode=' and row[0][0] != ':':
                pass
            if sRowType == ':IOAccess' and row[0][0] != ':':
                tIOAccess.append(row)
            if sRowType == ':AlarmGroup' and row[0][0] != ':':
                if bSystemGroup == False:
                    bSystemGroup = True
                    tSystemGroup[0] = 'System_%s' % (sFilenameSafe)
                    tSystemGroup[1] = '$System'
                    tSystemGroup[2] = 'Alarm Group for %s application' % (sFilename)
                    tAlarmGroup.append(tSystemGroup)
                if row[1] == '$System':
                    row[1] = 'System_%s' % (sFilenameSafe)
                tAlarmGroup.append(row)
            if sRowType == ':MemoryDisc' and row[0][0] != ':':
                if row[10] != 'None' and float(row[11]) <= 3:
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tMemoryDisc.append('"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,"%s",%s,%s,"%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            if sRowType == ':IODisc' and row[0][0] != ':':
                if row[10] != 'None' and float(row[11]) <= 3:
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tIODisc.append('"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,"%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tAccessNames, row[13])
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            if sRowType == ':MemoryInt' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tMemoryInt.append('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            if sRowType == ':IOInt' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tIOInt.append('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tAccessNames, row[42])
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            if sRowType == ':MemoryReal' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tMemoryReal.append('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            if sRowType == ':IOReal' and row[0][0] != ':':
                if  (row[16] == 'On' and float(row[18]) <= 3) or (row[19] == 'On' and float(row[21]) <= 3) or (row[22] == 'On' and float(row[24]) <= 3) or (row[25] == 'On' and float(row[27]) <= 3) or (row[28] == 'On' and float(row[30]) <= 3) or (row[31] == 'On' and float(row[33]) <= 3) or (row[35] == 'On' and float(row[37]) <= 3):
                    if row[1] == '$System':
                        row[1] ='System_%s' % (sFilenameSafe)
                    tIOReal.append('"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s",%s,"%s",%s,"%s",%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row))
                    fDuplicateCheck(tAccessNames, row[42])
                    fDuplicateCheck(tGroupNames, row[1])
                    tTagnamesFile.append(row[0])
            #if sRowType == ':MemoryMsg' and row[0][0] != ':':
            #    tMemoryMsg.append('"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':IOMsg' and row[0][0] != ':':
            #    tIOMsg.append('"%s","%s","%s",%s,%s,%s,%s,%s,"%s","%s",%s,"%s",%s,"%s","%s"\n' % tuple(row))
            #    fDuplicateCheck(tAccessNames, row[9])
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':GroupVar' and row[0][0] != ':':
            #    tGroupVar.append('"%s","%s","%s","%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':HistoryTrend' and row[0][0] != ':':
            #    tHistoryTrend.append('"%s","%s","%s","%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':TagID' and row[0][0] != ':':
            #    tTagID.append('"%s","%s","%s","%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':IndirectDisc' and row[0][0] != ':':
            #    tIndirectDisc.append('"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':IndirectAnalog' and row[0][0] != ':':
            #    tIndirectAnalog.append('"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row))
            #    tTagnamesFile.append(row[0])
            #if sRowType == ':IndirectMsg' and row[0][0] != ':':
            #    tIndirectMsg.append('"%s","%s","%s",%s,%s,%s,"%s"\n' % tuple(row))            
        for row in tIOAccess:
            for match in tAccessNames:
                if row[0] == match:
                    tIOAccessCorrected.append(row)                    
        for row in tGroupNames:
            for match in tAlarmGroup:
                if row == match[0]:
                    fDuplicateCheck(tGroupNames, match[1])
        tGroupNamesFiles.append([filename, tGroupNames])
        tTagnamesFiles.append([filename, tTagnamesFile])
        if len(tAlarmGroupCorrect) == 0:
            tAlarmGroupCorrect.append(tSystemGroup)
        for correct in tAlarmGroupCorrect:
            for order in tAlarmGroup:
                if correct[0] == order[1]:
                    for want in tGroupNames:
                        if order[0] == want:
                            tAlarmGroupCorrect.append(order)
stdOut += tTableHeaders[0]
stdOut += tTableHeaders[1]
for row in tIOAccessCorrected:
    stdOut += '"%s","%s","%s",%s,%s\n' % tuple(row)
stdOut += tTableHeaders[2]
for row in tAlarmGroupCorrect:
    stdOut += '"%s","%s","%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s","%s","%s"\n' % tuple(row)
stdOut += tTableHeaders[3]
for row in tMemoryDisc:
    stdOut += row
stdOut += tTableHeaders[4]
for row in tIODisc:
    stdOut += row
stdOut += tTableHeaders[5]
for row in tMemoryInt:
    stdOut += row
stdOut += tTableHeaders[6]
for row in tIOInt:
    stdOut += row
stdOut += tTableHeaders[7]
for row in tMemoryReal:
    stdOut += row
stdOut += tTableHeaders[8]
for row in tIOReal:
    stdOut += row
stdOut += tTableHeaders[9]
for row in tMemoryMsg:
    stdOut += row
stdOut += tTableHeaders[10]
for row in tIOMsg:
    stdOut += row
stdOut += tTableHeaders[11]
for row in tGroupVar:
    stdOut += row
stdOut += tTableHeaders[12]
for row in tHistoryTrend:
    stdOut += row
stdOut += tTableHeaders[13]
for row in tTagID:
    stdOut += row
stdOut += tTableHeaders[14]
for row in tIndirectDisc:
    stdOut += row
stdOut += tTableHeaders[15]
for row in tIndirectAnalog:
    stdOut += row
stdOut += tTableHeaders[16]
for row in tIndirectMsg:
    stdOut += row
fDuplicateTest(tGroupNamesFiles, tGroupNamesFilesDuplicate)
fDuplicateTest(tTagnamesFiles, tTagnamesFilesDuplicate)
if len(tGroupNamesFilesDuplicate) > 0 or len(tTagnamesFilesDuplicate) > 0:
    #if len(tGroupNamesFilesDuplicate) > 0:
    #    errorDump += 'Alarm Group name conflicts\n\n'
    #    for item in tGroupNamesFilesDuplicate:
    #        errorDump += 'Filename 1: ' + item[0] + '\nFilename 2: ' + item[1] + '\nAlarm Group: ' + item[2] + '\n\n'
    #    errorDump += '\n\n' 
    if len(tTagnamesFilesDuplicate) > 0:    
    #    errorDump += 'Tagname conflicts\n\n'
        for item in tTagnamesFilesDuplicate:
    #        errorDump += 'Filename 1: ' + item[0] + '\nFilename 2: ' + item[1] + '\nTagname: ' + item[2] + '\n\n' 
            errorDump += item[2] + '\n'
    with open('c:/mods/' + 'errors.txt', 'w') as file:
        file.write(errorDump)
else:
    with open('c:/mods/' + 'alarmappload.csv', 'w') as file:
        file.write(stdOut)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")