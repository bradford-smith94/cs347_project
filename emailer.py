import smtplib
from email.mime.text import MIMEText
import csv


def sendmail (recipients, person, count):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    #email info, must be gmail.  (email, password)
    server.login("JohnSmith@gmail.com", "")
    print (recipients[count][2])
    message = person + msg
    try:
        print (message.as_string)
        server.sendmail("email", recipients[count][2], message.as_string)
    except:
        print ("message to %s did not send" %(recipients[count]))
    server.quit()
    count += 1

def getRecipients():
    emails = []
    #put file name in here.
    with open('test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            emails.append(row)
    return(emails)


recipients = []
recipients = getRecipients()

textfile = "test.txt"
txt = open(textfile, "r")
msg = MIMEText(txt.read())
txt.close()
print (msg)
msg["Subject"] = ""
msg["From"] = ""
msg["To"] = ""
count = 1
for x in recipients:
    if count == len(recipients):
        break
    #having trouble with this part.  it will send by I can not figure out how to send it without google reporting it as spam.
    person = MIMEText ("Dear %s %s" %(recipients[count][1], recipients[count][0]))
    sendmail(recipients, person, count)
    count += 1
