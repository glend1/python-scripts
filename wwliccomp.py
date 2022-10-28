import csv, re, time
startTime = time.clock()
tKnownLicences, tSolutionsLicences, unknown, productCodes, stdOut = [], [], [], [], ''
def compareLic(source, target, errorGroup):        
    for known in source:
        sourceTracker = True
        knownMatch = re.search('^[0-9]+', known[0])
        if knownMatch:
            knownSerial = knownMatch.group(0)
        else:
            continue #goes to next line in the list to stop errors later on
        for solutions in target:
            solutionsMatch = re.search('^[0-9]+', solutions[0])
            if solutionsMatch:
                solutionsSerial = solutionsMatch.group(0)
            else:
                continue #goes to next line in the list to stop errors later on
            if knownSerial == solutionsSerial:
                if known[1] != solutions[1]:
                    #perform self check
                    finalCheck = True
                    for finalItems in unknown:
                        finalMatch = re.search('^[0-9]+', finalItems[0])
                        if finalMatch:
                            finalSerial = finalMatch.group(0)
                        else:
                            continue #goes to next line in the list to stop errors later on
                        if finalSerial == knownSerial:
                            finalCheck = False
                            continue
                    if finalCheck == True:
                        if solutions[0] == known[0]:
                            known.append('Different Product Key!')
                        else:
                            known.append('An Upgrade Has Occurred. {0}; {1}; {2}'.format(solutions[0], solutions[1], solutions[2]))
                        unknown.append(known)
                    if len(unknown) == 0:
                        if solutions[0] == known[0]:
                            known.append('Different Product Key!')
                        else:
                            known.append('An Upgrade Has Occurred. {0}; {1}; {2}'.format(solutions[0], solutions[1], solutions[2]))
                        unknown.append(known)
                sourceTracker = False
                break
        if sourceTracker == True:
            known.append('Missing Product From %s List!' % errorGroup)
            unknown.append(known)
with open('wwlic.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        tKnownLicences.append(row)
with open('c:/wwnewlic.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        tSolutionsLicences.append(row)
compareLic(tKnownLicences, tSolutionsLicences, 'Solutions')
compareLic(tSolutionsLicences, tKnownLicences, 'JMs')
#for listItem in unknown:
#    stdOut += '"{0}","{1}","{2}","{3}"\n'.format(listItem[0], listItem[1], listItem[2], listItem[-1])
#with open('c:/wwlicdiff.csv', 'w') as file:
#        file.write(stdOut)
for codes in productCodes:
    print(codes)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")