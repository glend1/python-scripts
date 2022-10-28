
import time, csv
startTime = time.clock()
word = ['PLC16']
def fPlcFilter(match):
    for x in word:
        if x == match:
            return True
sFile = r'c:/glen.csv'
with open(sFile, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    stdOut = ''
    for row in reader:
            stdOut += '%s\t%s\tts2\tserver_runtime\tplc16\t%s\tIOServer\tDelta\t0\t1000\t30\t0\tAll\tNone\t%s\t%s\t0\t100000\tNone\tMSFloat\t0\t\t0\t0\t0\t0\tSystem Default\t0\tNo\tTimeValue\n' % (row[0], row[2], row[44], row[12], row[13])
with open(r'c:/mod.csv', 'w') as file:
    file.write(stdOut)
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")
#row[0],row[2],'ts2','server_runtime','plc16',row[45],'IOServer','Delta',0,1000,30,0,'All',row[10],row[14],row[15],0,100000,'Linear','MSFloat',0,'',0,0,0,0,'System','Default',0,'No','TimeValue'                                                                                                                                                        