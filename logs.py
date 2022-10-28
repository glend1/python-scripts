import time, csv, os
startTime = time.clock()
title = 'Illuminator Usage Report'
stdOut = ''
sFolder = r'c:/report/logs/'
dailyArr = []
dailyIps = []
minArr = []
avgArr = []
maxArr = []
for x in os.listdir(sFolder):
    fileArr = sFolder + x
    hourArr = []
    dayArr = []
    for i in range(24):
        hourArr.append([])
    with open(fileArr, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            if row[0][0] == '#':
                next(reader)
                continue
            timeObj = time.strptime(row[1], "%H:%M:%S")
            date = row[0]
            ip = row[2]
            isDayTested = 0
            if dayArr == []:
                dayArr.append(ip)
                if dailyIps == []:
                    dailyIps.append(ip)
            for h in dayArr:
                if h == ip:
                    isDayTested = 1
                    break
            if isDayTested != 1:
                dayArr.append(ip)
                isDailyTested = 0
                for l in dailyIps:
                    if l == ip:
                        isDailyTested = 1
                        break
                if isDailyTested != 1:
                    dailyIps.append(ip)
            isHourTested = 0
            if hourArr[timeObj.tm_hour] == []:
                hourArr[timeObj.tm_hour].append(ip)
            for j in hourArr[timeObj.tm_hour]:
                if j == ip:
                    isHourTested = 1
                    break
            if isHourTested != 1:    
                hourArr[timeObj.tm_hour].append(ip)
    output = True
    if output == True:
        dailyArr.append(len(dayArr))
        day = ''
        for z in dayArr:
            day += z + ', '
        # day for iplist
        stdOut += '<table><thead><tr><th colspan=\'25\'>' + 'Date: ' + date + '<span class=\'filename\'>Filename: ' + x + '</span></th></tr></thead>'
        hour = 0
        countArr = []
        stdOut += '<tbody><tr><td class=\'legend\'>Hour</td>'
        for c in range(24):
            stdOut += '<td>' + str(c) + '</td>'
        stdOut += '</tr><tr><td class=\'legend\'># IPs</td>'
        for x in hourArr:
            iplist = ''
            countArr.append(len(x))
            for y in x:
                iplist += y + ', '
            stdOut += '<td>' + str(len(x)) + '</td>'
            #stdOut += 'hour of the day (in 24h):' + str(hour) + 'h number of unique ips:' + str(len(x)) + '<br />ip list:' + iplist + '<br /><br />'
            hour += 1
        stdOut += '</tr></tbody>'
        avg = 0
        for k in countArr:
            avg += k
        avg = round(avg / len(countArr), 2)
        stdOut += '<tfoot><tr><td colspan=\'25\'>Min: ' + str(min(countArr)) + '&nbsp;&nbsp;&nbsp;&nbsp;Avg: ' + str(avg) + '&nbsp;&nbsp;&nbsp;&nbsp;Max: ' + str(max(countArr)) + '&nbsp;&nbsp;&nbsp;&nbsp;Total: ' + str(len(dayArr)) + '</td></tr></tfoot></table>'
        minArr.append(min(countArr))
        avgArr.append(avg)
        maxArr.append(max(countArr))
        #stdOut += 'lowest number of unique ips per hour:' + str(min(countArr)) + '<br />average number of unique ips per hour:' + str(avg) + '<br />highest number of unique ips per hour:' + str(max(countArr)) + '<br />' + 'number of unique ips:' + str(len(dayArr)) + '<br />'
d = 0
cells = 6
dailyIpList = '<table><thead><tr><th colspan=\'' + str(cells) + '\'>List of IPs connected over Sample</th></tr></thead><tbody>'
for b in dailyIps:
    if d % cells == 0:
        dailyIpList += '<tr>'
        cellsWritten = 0
    dailyIpList += '<td>' + b + '</td>'
    cellsWritten += 1
    if d % cells == cells - 1:
        dailyIpList += '</tr>'
    d += 1
manualComplete = 0
while cellsWritten < cells:
    dailyIpList += '<td></td>'
    cellsWritten += 1
    manualComplete = 1
if manualComplete == 1:
    dailyIpList += '</tr>'

dailyAvg = 0
for a in dailyArr:
    dailyAvg += a
dailyAvg = int(round(dailyAvg / len(dailyArr), 0))
#stdOut += '<p>Lowest number of unique IPs per day: ' + str(min(dailyArr)) + '<br />Average number of unique IPs per day: ' + str(dailyAvg) + '<br />Highest number of unique IPs per day: ' + str(max(dailyArr)) + '</p>'
#stdOut += '<p>Number of unique IPs in total: ' + str(len(dailyIps)) + '</p>'
avg = 0
for k in avgArr:
    avg += k
avg = round(avg / len(avgArr), 2)
dailyIpList += '</tbody><tfoot><tr><td colspan=\'' + str(cells) + '\'>Min: ' + str(min(minArr)) + '&nbsp;&nbsp;&nbsp;&nbsp;Avg: ' + str(avg) + '&nbsp;&nbsp;&nbsp;&nbsp;Max: ' + str(max(maxArr)) + '&nbsp;&nbsp;&nbsp;&nbsp;Total: ' + str(len(dailyIps)) + '</td></tr></tfoot></table>'
stdOut +=  dailyIpList
with open('c:/report/usagereport.html', 'w') as file:
    file.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN""http://www.w3.org/TR/html4/loose.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-GB" lang="en-GB">
        <head>
            <link rel="stylesheet" href="stylesheet.css" type="text/css" />
            <title>''' + title + '''</title>
        </head>
        <body>
            <h1>''' + title + '</h1>')
    file.write(stdOut)
    file.write('''</body>
    </html>''')
print('Finished in ' + str(int(round(time.clock() - startTime, 0))) + " seconds")