# Secure_Sockets_Layer.py
from socket import *
from base64 import *
import ssl


# #Collect required user input:
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

# Collect required user input hardcode
EMAIL_ADDRESS = "hellowordLabs@gmail.com"
EMAIL_PASSWORD = ""  # uses an app password
EMAIL_DESTINATION = "hellowordLabs@gmail.com"
EMAIL_SUBJECT = "Hello"
EMAIL_BODY = "I love computer networks!"

# Message to send
msg = EMAIL_BODY
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = 
#Fill in start 

mailserver = ("smtp.gmail.com",587)

# #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
 
# Fill in start

# Account Authentication
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
recv22 = clientSocket.recv(1024)
sslClientSocket = ssl.wrap_socket(clientSocket)

THIS_ADDRESS = b64encode(EMAIL_ADDRESS.encode())
THIS_PASSWORD = b64encode(EMAIL_PASSWORD.encode())

authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd.encode())
recv22 = sslClientSocket.recv(1024)
#print(recv22)

sslClientSocket.send(THIS_ADDRESS + b"\r\n")
recv23 = sslClientSocket.recv(1024)
#print(recv23)

sslClientSocket.send(THIS_PASSWORD + b"\r\n")
recv24 = sslClientSocket.recv(1024)
#print(recv24)

mailFrom = f'MAIL FROM: <{EMAIL_ADDRESS}>\r\n'
sslClientSocket.send(mailFrom.encode())
recv2 = sslClientSocket.recv(1024).decode()
print(recv2)


# Fill in end

# Send RCPT TO command and print server response.

# Fill in start

rcptToCommand = f'RCPT TO: <{EMAIL_DESTINATION}>\r\n'
sslClientSocket.send(rcptToCommand.encode())
recv3 = sslClientSocket.recv(1024).decode()
print(recv3)

# Fill in end

# Send DATA command and print server response.

# Fill in start

dataCommand = 'DATA\r\n'
sslClientSocket.send(dataCommand.encode())
recv4 = sslClientSocket.recv(1024).decode()
print(recv4)

# Fill in end

# Send message data.

# Fill in start

sslClientSocket.send(f"Subject: {EMAIL_SUBJECT}\n\n{msg}".encode())

# Fill in end

# Message ends with a single period.

# Fill in start

sslClientSocket.send(endmsg.encode())
recv5 = sslClientSocket.recv(1024).decode()
print(recv5)

# Fill in end

# Send QUIT command and get server response.

# Fill in start

quitCommand = 'QUIT\r\n'
sslClientSocket.send(quitCommand.encode())
recv6 = sslClientSocket.recv(1024).decode()
print(recv6)
sslClientSocket.close()

# Fill in end