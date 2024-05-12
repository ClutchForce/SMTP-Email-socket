# smtplib_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# # #Collect required user input:
# #The users email address
# EMAIL_ADDRESS = input("Enter Your Email Address: ")
# #The users password 
# EMAIL_PASSWORD = input("Enter Your Password: ")
# #The email's destination email address 
# EMAIL_DESTINATION = input("Enter Destination Email Address: ")
# #The email's subject 
# EMAIL_SUBJECT = input("Enter Email Subject: ")
# #The email's body
# EMAIL_BODY = input("Enter Email Message: ")

# # Collect required user input hardcode
EMAIL_ADDRESS = "hellowordLabs@gmail.com"
EMAIL_PASSWORD = ""  # uses an app password
EMAIL_DESTINATION = "hellowordLabs@gmail.com"
EMAIL_SUBJECT = "Hello2"
EMAIL_BODY = "I love computer networks!"

# Create a MIMEText object to represent your email
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_DESTINATION
msg['Subject'] = EMAIL_SUBJECT

# Attach the body of the email to the MIMEText object
msg.attach(MIMEText(EMAIL_BODY, 'plain'))

try:
    # Set up the SMTP client
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, EMAIL_DESTINATION, msg.as_string())
    server.quit()
    print("Email sent successfully")

except Exception as e:
    print(f"Failed to send email: {e}")