import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg.set_unixfrom('author')
msg['From'] = 'YourGoDaddyemail@email.com' 
msg['To'] = 'ReceiversAddress@email.com' 
msg['Subject'] = 'Jinhe mera dil luteyaa'
message = 'OHHOOO'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465) #Port 465 will be used
mailserver.ehlo()
mailserver.login('YourGoDaddyemail@email.com', 'godaddypassword') #Email and password

mailserver.sendmail('YourGoDaddyemail@email','ReceiversAddress@email.com',msg.as_string())

mailserver.quit()
