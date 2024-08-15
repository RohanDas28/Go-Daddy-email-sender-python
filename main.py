import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    msg = MIMEMultipart()
    msg.set_unixfrom('author')
    msg['From'] = 'YourGoDaddyemail@email.com' 
    msg['To'] = 'ReceiversAddress@email.com' 
    msg['Subject'] = 'Jinhe mera dil luteyaa'
    message = 'OHHOOO'
    msg.attach(MIMEText(message))

    # Connect to the server
    mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    mailserver.ehlo()  # Say hello to the server
    # Login to the server
    mailserver.login('YourGoDaddyemail@email.com', 'godaddypassword')
    # Send the email
    mailserver.sendmail('YourGoDaddyemail@email.com', 'ReceiversAddress@email.com', msg.as_string())
    # Disconnect from the server
    mailserver.quit()
    print("Email sent successfully!")

except smtplib.SMTPServerDisconnected as e:
    print(f"SMTPServerDisconnected: {e}")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTPAuthenticationError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
