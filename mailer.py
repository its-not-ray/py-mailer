from email.message import EmailMessage
from email import message
from os import system, name
import smtplib
import shutil
import signal
import sys
import set
import time

# custom instagram mail info
class mssgs():
    def __init__(self, toadress, username, subj, body):
        self.toadtess = toadress
        self.username = username
        self.subj = subj
        self.body = body
mail = mssgs

# manage phishing option details
def phishing_input():
    # basic info input
    mail.username = input("target username: ")
    mail.toadress = input("target gmail: ")
    if len(mail.toadress) < 15:
        print("gmail address not found.\nPlease input a valid gmail\n")
        exit()
    phishing_link = input("phishing link: ")

    # fake mail details
    mail.subj = f"{mail.username}, We've made it easy to get back on Instagram"
    mail.body = f"Hi {mail.username},\nSorry to hear you're having trouble logging into Instagram. We got a message that you forgot \
your password. If this was you, you can use the link bellow to reset your password.\n\n{phishing_link}\n\nIf you didn't request a password\
 reset link you can ignore this message.\nOnly people who know your Instagram password can log into your account\n\nThis message was sent \
to {mail.toadress} and intended for {mail.username}"

# main
def main():
    print("Disclamier:\nYour sender gmail needs to have (Access to less secure apps) enabled\nYou can check here:\
 https://www.google.com/settings/security/lesssecureapps\n")

# multi reciever option
    #multi_account = False
    #while True:
    #    numberofaccounts = input("To how many accounts do you want to send this mail to? ")
    #    if numberofaccounts.isnumeric() == True:
    #        if int(numberofaccounts) > 10:
    #            print("Max number allowed is 10.\n")
    #        else:
    #            break
    #    else:
    #        print("Please input an integer.\n")

# choose custom
    switch.custom_Insta_message = False # insta set switch
    switch.default_message = False # default set switch

    question = input("Choose an option\n[01] Send custom mail\n[02] Send instagram phishing mail\n") # custom or set option
    if question == "01" or question == "1": # default option
        switch.default_message = True
        switch.custom_Insta_message = False
    elif question == "02" or question == "2": # instagram option
        switch.custom_Insta_message = True
        switch.default_message = False
# incorrect input, exit
    else:
        question = '"{0}"'.format(question)
        print("\nNot even jay is that dumb...\nTHERE IS NO", question, "OPTION, Idiot!")
        exit()

# get target gmail or target instagram info depending on prevous option
    if switch.default_message == True: # default option
        to_address = input("Target gmail: ")
        if len(to_address) < 15:
            print("gmail address not found.\nPlease input a valid gmail\n")
            exit()
    elif switch.custom_Insta_message == True: # custom instagram option
        phishing_input()

# senders info + message info
    try:
        username = set.senders_emails[0]
        password = set.senders_passwords[0]
        if switch.default_message == True:
            message_s = set.message_subject[0]
            message_b = set.message_content[0]
        elif switch.custom_Insta_message == True:
            message_s = mail.subj
            message_b = mail.body
        else:
            print("Something went wrong, please try again.")
            exit()
    except:
        print("set folder empty")
        exit()
    valid_set_check(username, password)

# recievers info + mssg
    if switch.default_message == True:
        fromaddr = '' 
        msg =  EmailMessage()
        msg.set_content(message_b)
        msg['Subject'] = message_s
        msg['from'] = username
        msg['to'] = to_address
    elif switch.custom_Insta_message == True:
        fromaddr = '' 
        msg =  EmailMessage()
        msg.set_content(mail.body)
        msg['Subject'] = mail.subj
        msg['from'] = mail.username
        msg['to'] = mail.toadress

# sending mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.ehlo()
        server.starttls()
    except:
        print("Network error, please check your internet connection")
        exit()
    try:
        server.login(username, password)
        server.send_message(msg) 
        server.quit()
        fun_output()
    except:
        print("Error: This error could have been prompted due to:\n- The gmail you are trying to send this mail to is invalid.\n\
- Authentication error, make sure you have (allow less secure applications \
to access you account) turned on.\n- Make sure your username and password are correct.")
        exit()

class switches():
    def __init__(switch):
        switch.reset_all = False
        switch.reset_gmail = False
        switch.reset_content = False
        switch.custom_Insta_message = False
        switch.default_message = False

switch = switches()
def reset_options():
    # reset options
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
        print("\nNot even jay is that dumb...\nTHERE IS NO", question, "OPTION, Idiot!")
        exit()

# checks if sender gmail and password are valid
def valid_set_check(gmail, password):
    if len(gmail) < 15 and len(password) < 5:
        print("Invalid settings, sender credentials invalid.\n\n Try:\n- pthon3 main.py -set\n- 02")
        exit()
    elif len(gmail) < 15:
        print("Invalid settings, sender gmail invalid\n\nTry:\n- pthon3 main.py -set\n- 02")
        exit()
    elif len(password) < 5:
        print("Invalid settings, sender gmail password invalid\n\nTry:\n- pthon3 main.py -set\n- 02")
        exit()

# reset function for settings (independent reset settings available)
def reset_set():
    reset_options()
    if switch.reset_all == True:
    # taking input for reset
        gmail = input("gmail: ") 
        gmail_pass = input("password: ")
        mssg_sub = input("subject: ")
        mssg_content = input("body: ")

    # changing input into correct format
        gmail = ('"{0}"'.format(gmail))
        gmail_pass = ('"{0}"'.format(gmail_pass))
        mssg_content = ('"{0}"'.format(mssg_content))
        mssg_sub = ('"{0}"'.format(mssg_sub))
        default_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
\n\n# supports multiple emails\nsenders_emails = [{gmail}]\nsenders_passwords = [{gmail_pass}]\n\n# supports multiple \
messages\nmessage_content = [{mssg_content}]\nmessage_subject = [{mssg_sub}]"

    # writing new settings
        file = open("set.py", "w")
        file.truncate()
        file.write(default_set)
        file.close()
    elif switch.reset_gmail == True:
    # saving all needed data
        prevous_mssg = set.message_content[0]
        prevous_subj = set.message_subject[0]
        prevous_mssg = '"{0}"'.format(prevous_mssg)
        prevous_subj = '"{0}"'.format(prevous_subj)
    # getting new data
        gmail = input("gmail: ") 
        gmail_pass = input("password: ")
        gmail = ('"{0}"'.format(gmail))
        gmail_pass = ('"{0}"'.format(gmail_pass))
        costom_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
\n\n# supports multiple emails\nsenders_emails = [{gmail}]\nsenders_passwords = [{gmail_pass}]\n\n# supports multiple \
messages\nmessage_content = [{prevous_mssg}]\nmessage_subject = [{prevous_subj}]"

    # writing new settigns
        file = open("set.py", "w")
        file.truncate()
        file.write(costom_set)
        file.close()
    elif switch.reset_content == True:
    # saving all needed data
        prevous_gmail = set.senders_emails[0]
        prevous_pass = set.senders_passwords[0]
        prevous_gmail = '"{0}"'.format(prevous_gmail)
        prevous_pass = '"{0}"'.format(prevous_pass)
    # getting new data
        mssg_sub = input("subject: ")
        mssg_content = input("body: ")
        mssg_content = ('"{0}"'.format(mssg_content))
        mssg_sub = ('"{0}"'.format(mssg_sub))
        costom_set = f"# THIS FILE IS NOT TO BE EXECUTED\n# THIS FILE IS TO BE EDITED ONLY FROM main.py\
\n\n# supports multiple emails\nsenders_emails = [{prevous_gmail}]\nsenders_passwords = [{prevous_pass}]\n\n# supports multiple \
messages\nmessage_content = [{mssg_content}]\nmessage_subject = [{mssg_sub}]"
    # writing new settigns
        file = open("set.py", "w")
        file.truncate()
        file.write(costom_set)
        file.close()

# prints out current settings for user
def show_set():
    try:
        print("current sender email: ", set.senders_emails[0])
        print("current email password: ", set.senders_passwords[0])
        print("current mssg subj: ", set.message_subject[0])
        print("current mssg content: ", set.message_content[0])
    except:
        print("Set folder empty")
        exit()

# screen fun time
def fun_output():
    columns = shutil.get_terminal_size().columns
    output = [" Thank you for using mailer!", "script by:", "its-not-ray on Github"]
    temp = "##"
    print("\n\n")
    for x in range(6):
        print(temp.center(columns))
        temp = temp *2
    for x in range(3):
        print(output[x].center(columns))

# terminal clear function
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# exit function
def byby():
    def signal_handler(sig, frame):
        clear()
        print("I'll be waiting for you on the dark side...")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
byby()

# usage
NOA = len(sys.argv)
if NOA == 1: # run script w\ current set
    print("Command not found\nFor help run: ./mailer.py -h")
elif NOA == 2:
    if sys.argv[1] == "-execute":
        main()
# get help
    elif sys.argv[1] == "-h": 
        print("DISCLAIMER: All command must start with, python3 ./mailer.py...\nusage:\n-exec\
ute (run script with old settings)\n-set (change settings)\n-show -set (show current settings)\
\n--version (show py-mailer current version)")
# reset settings file
    elif sys.argv[1] == "-set": 
        reset_set()
    elif sys.argv[1] == "--version":
        print("py-mailer v1.0")
    else:
        print("For help run: ./mailer.py -h")
elif NOA == 3:
    if sys.argv[1] == "-show" and sys.argv[2] == "-set":
        show_set()
