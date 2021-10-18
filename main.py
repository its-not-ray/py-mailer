from email.message import EmailMessage
from email import message
import smtplib
import sys
import set
import time


def main():
    to_address = input("Target gmail: ")

    username = set.senders_emails[0]
    password = set.senders_passwords[0]
    message_s = set.message_subject[0]
    message_b = set.message_content[0]

    fromaddr = '' 
    msg =  EmailMessage()
    msg.set_content(message_b)
    msg['Subject'] = message_s
    msg['from'] = username
    msg['to'] = to_address

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.send_message(msg) 
    print("mail sent")
    print("done")
    server.quit()

class switches():
    def __init__(switch):
        switch.reset_all = False
        switch.reset_gmail = False
        switch.reset_content = False

switch = switches()
def reset_options():
    switch.reset_all = False
    switch.reset_gmail = False
    switch.reset_content = False

    question = input("What do you wish to reset?\n[01] All\n[02] Sender gmail\n[03] Mail content\n")
    if question == "01" or question == "1":
        switch.reset_all = True
    elif question == "02" or question == "2":
        switch.reset_gmail = True
    elif question == "03" or question == "3":
        switch.reset_content = True
    else:
        question = '"{0}"'.format(question)
        print("\nHAHAHAHAAHAHAHA ARE YOU BLIND? THERE IS NO", question, "OPTION\nIdiot")

def reset_set():
    reset_options()
    if switch.reset_all == True:
        gmail = input("gmail: ") 
        gmail_pass = input("password: ")
        mssg_sub = input("subject: ")
        mssg_content = input("body: ")
        gmail = ('"{0}"'.format(gmail))
        gmail_pass = ('"{0}"'.format(gmail_pass))
        mssg_content = ('"{0}"'.format(mssg_content))
        mssg_sub = ('"{0}"'.format(mssg_sub))
        default_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
        \n\n# supports multiple emails\nsenders_emails = [{gmail}]\nsenders_passwords = [{gmail_pass}]\n\n# supports multiple \
messages\nmessage_content = [{mssg_content}]\nmessage_subject = [{mssg_sub}]"

        file = open("set.py", "w")
        file.truncate()
        file.write(default_set)
        file.close()
    elif switch.reset_gmail == True:
        prevous_mssg = set.message_content[0]
        prevous_subj = set.message_subject[0]
        prevous_mssg = '"{0}"'.format(prevous_mssg)
        prevous_subj = '"{0}"'.format(prevous_subj)
        gmail = input("gmail: ") 
        gmail_pass = input("password: ")
        gmail = ('"{0}"'.format(gmail))
        gmail_pass = ('"{0}"'.format(gmail_pass))
        costom_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
        \n\n# supports multiple emails\nsenders_emails = [{gmail}]\nsenders_passwords = [{gmail_pass}]\n\n# supports multiple \
messages\nmessage_content = [{prevous_mssg}]\nmessage_subject = [{prevous_subj}]"

        file = open("set.py", "w")
        file.truncate()
        file.write(costom_set)
        file.close()
    elif switch.reset_content == True:
        prevous_gmail = set.senders_emails[0]
        prevous_pass = set.senders_passwords[0]
        prevous_gmail = '"{0}"'.format(prevous_gmail)
        prevous_pass = '"{0}"'.format(prevous_pass)
        mssg_sub = input("subject: ")
        mssg_content = input("body: ")
        mssg_content = ('"{0}"'.format(mssg_content))
        mssg_sub = ('"{0}"'.format(mssg_sub))
        costom_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
        \n\n# supports multiple emails\nsenders_emails = [{prevous_gmail}]\nsenders_passwords = [{prevous_pass}]\n\n# supports multiple \
messages\nmessage_content = [{mssg_content}]\nmessage_subject = [{mssg_sub}]"
        file = open("set.py", "w")
        file.truncate()
        file.write(costom_set)
        file.close()

NOA = len(sys.argv)
if NOA == 1: # run script w\ current set
    print("Command not found\nFor help run: ./main -h")
elif NOA == 2:
    if sys.argv[1] == "-execute":
        main()
    elif sys.argv[1] == "-h": 
        print("usage:\nTo run script with old settings: ./main.py -execute\nTo change settings: ./main.py -r")
    elif sys.argv[1] == "-r": 
        reset_set()
    else:
        print("For help run: ./main -h")
 
