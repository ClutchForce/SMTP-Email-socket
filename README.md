# SMTP Mail Client in Python

This project involves developing a simple mail client that sends emails using the SMTP protocol without relying on high-level libraries like `smtplib` initially, to deepen the understanding of SMTP and socket programming. This client connects directly to a mail server, dialogues using SMTP commands, and sends an email message.

## 📚 Project Description

In this project, I gain a practical understanding of the SMTP protocol by implementing a Python script that interacts with a mail server to send emails. This approach helps you understand the low-level details of mail sending operations over the internet.

## 🛠️ SMTP Client Implementation

You are provided with skeleton code that requires completion to function. The SMTP interactions are handled manually through raw socket connections, providing hands-on experience with SMTP commands and responses.

### Manual SMTP Interaction

Here's a breakdown of tasks implemented in the raw SMTP client:

- **Connect to Mail Server**: Establish a TCP connection to the SMTP server.
- **SMTP Dialogue**: Communicate using SMTP commands to send an email.
- **Secure Connection**: Implement TLS/SSL to encrypt the communication with the server.

## 📧 Using `smtplib`

After understanding the raw SMTP interactions, the task shifts to using Python's `smtplib`, which simplifies sending emails but abstracts away the details.

### `smtplib` Email Client

This script simplifies email sending by managing socket connections and SMTP dialogues internally:

- **Setup Connection**: Uses `smtplib.SMTP` to handle server connection.
- **Security**: Implements `starttls()` to secure the email transmission.
- **Send Email**: Simplifies sending emails with minimal code.

## 📕 Conclusion

This project highlights the complexity and intricacy of SMTP communication. It provides a clear understanding of how emails are transmitted over the internet and the role of protocols like SSL/TLS in securing these communications.