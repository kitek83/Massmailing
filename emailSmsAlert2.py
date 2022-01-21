import smtplib
from email.message import EmailMessage

USER =input('Enter your gmail: ') # insert your valid google account
PASSWORD = input('Enter the password generated in app passwords from your google account: ')  # go to google accounts app passwords and generate password

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = USER
    msg['from'] = user
    password = PASSWORD

    # settingg the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # for gmail requirements
    server.login(user, password)

    #sending the message
    server.send_message(msg)

    server.quit()

    print(f'Your message is: {msg}')


if __name__ == '__main__':

    emails_to = [''] #enter emails of receiveers as a list
    body = 'Hello thi is body of this message!\nYou can write whatever you want!'
    subject = 'Hey3'
    # looping enables massmeiling to emails_to
    for email in emails_to:
        email_alert(subject, body, email)