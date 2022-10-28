import pyodbc
import smtplib
server = 'BEAMEX-PC\CMXSQLEXPRESS'
db = 'Beamex'
uid = 'Auto'
pwd = 'Auto'
sqlConn = pyodbc.connect('DRIVER={SQL Server};Server=%s;Database=%s;UID=%s;PWD=%s;' % (server, db, uid, pwd))
sqlCur = sqlConn.cursor()
sQuery = ''
sqlQuery = 'select name, isactive from calprocedure where funccode = 12'
sqlCur.execute(sqlQuery)
sqlRows = sqlCur.fetchall()
sQuery += '<p>Server: %s<br />Database: %s<br />Username: %s<br />Password: %s<br />Query: %s</p><table border="1"><tr>\n' % (server, db, uid, pwd, sqlQuery)
for i in sqlRows[0].cursor_description:
    sQuery += '<td><b>' + i[0] + '</b></td>\n'
sQuery += '</tr>\n'
for row in sqlRows:
    sQuery += '<tr>\n'
    for i in row:
        sQuery += '<td>' + str(i) + '</td>\n'
    sQuery += '</tr>\n'
sQuery += '</table><b>with %s rows</b>\n' % str(len(sqlRows))
sqlCur.close()
eFrom = 'brimcontrols@matthey.com'
eTo = ['glen@cogentautomation.co.uk']
eMsg = """Content-Type: text/html
MIME-Version: 1.0
From: Brimsdown Process Controls <brimcontrols@matthey.com>
To: Glen Dovey <glen@cogentautomation.co.uk>
Reply-To: Charlie Dovey <doveyc@matthey.com>
Subject: Brimsdown Process Control Mail Notifications


""" + sQuery
eMail = smtplib.SMTP('172.30.4.15:25')
print(sQuery)
#eMail.sendmail(eFrom, eTo, eMsg)
eMail.quit()