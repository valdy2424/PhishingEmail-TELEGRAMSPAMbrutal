import asyncio
import logging
import re
import time
import os
import sys
import random
import socket

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime


# Get your own values from my.telegram.org
print  ("Selamat menggunakan tools Brutal ini<<<<<<anjay")
print  ("Get your own values from my.telegram.org")
hiks = input ("api_id   =")
hoks = input ("api_hash =")

api_id = hiks
api_hash = hoks


hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
hp = input('masukan no hp  use international +..?:')
# Ambil input dari user
cname = input("nama1: ")
crot = input("link1: ")


# buka file untuk ditulis
cname = open("cname.txt", "a")


os.path.exists('cname.txt')
cname = open("cname.txt")
# bot 2
# Ambil input dari user
cname2 = input("nama: ")
crot2 = input("link: ")


# buka file untuk ditulis
cname2 = open("cname2.txt", "a")


os.path.exists('cname2.txt')
cname2 = open("cname2.txt")

kontol = input('masukan pesan:')
memek  = input('masukan pesan bot2:')

def print_msg_time(message):
        print( f'{datetime.now().strftime("%H:%M:%S")}' +   f'{message}')

async def main():
        print ('kontol')
        print(' ======================================== \n')

        # Check if phone number is not specified
       
        phone_number = hp
        choice = kontol
        choice2 = memek
        if not os.path.exists("session"):
                os.mkdir("session")

    # Connect to client
        client = TelegramClient('session/' + phone_number, api_id, api_hash)
        await client.start(phone_number)
        me = await client.get_me()

        # start Robot

        print_msg_time(f'Name                  : {me.first_name}'   )
        print_msg_time( f'Welcome               : {me.first_name} - {me.last_name} ' )
        print_msg_time( f'Name                  : {me.first_name}'  )
        print_msg_time( f'Welcome               : {me.first_name} ')
        print(f'\n')
        print(f'Your  Name is       :' + hostname )   #get name 
        print(f'Your  IP Address is :' + IPAddr )#get ip
        print(f'\n')
        print_msg_time('Start Bot 1' + '\n' )
        print_msg_time('Start Bot 2' + '\n' )
       
        # Start command 

        i = 1
        while(True):
                await client.send_message(crot2, choice2)
                print_msg_time(f' Spam terkirim ke, {cname2}, Tunggu 30 detik to spamm {crot} Dengan Link = ' + choice2)
                time.sleep(0) #waktu klik hitungan dalam detik
                await client.send_message(crot, choice)
                print_msg_time(' Keterangan hasil klaim dari bot telegramnya---' )
                time.sleep(0) #waktu klik hitungan dalam detik
                i = 1

                # Message the bot
        @client.on(events.NewMessage(chats=cname2, incoming=True))
        async def earned_amount(event):
                message = event.raw_text
                if 'Balance' in message:
                        print_msg_time(event.raw_text + '\n' )
        await client.run_until_disconnected()

                # message bot 2
        @client.on(events.NewMessage(chats=cname, incoming=True))
        async def earned_amount(event):
                message = event.raw_text
                if 'Balance' in message:
                        print_msg_time(event.raw_text + '\n' )
        await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())

