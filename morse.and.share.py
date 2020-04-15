# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:43:18 2020

@author: eliss
"""
from time import sleep
import winsound
import smtplib
import ssl


MORSE_CODE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', " ": "/"}

# Function that translates text to morse code

def tomorse():
    message = input("Enter your message:")
    code = [MORSE_CODE[i.upper()] + " " for i in message if i.upper() in MORSE_CODE.keys()]
    ciph = "".join(code)
    print(ciph)
    for c in ciph:
        if c == ".":
            winsound.Beep(1000, 400)    # Here you can change (frequence, duration) of the beep
        elif c == "-":
            winsound.Beep(1000, 850)
        else:
            sleep(0.7)

    jo = input("If you want to translate morse code back to text, press 1. If you want to send the morse code via email, press 2. If you want to quit, press any key.")
    if jo == "1":
        print(fromorse())

    # Send morse code via email

    elif jo == "2":
        email1 = input("Enter your email: ")
        email2 = input("Enter the receiver email: ")
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = email1  # Enter your address
        receiver_email = email2  # Enter receiver address
        password = input("Type your password and press enter: ")
        message = ciph + " This message was sent from Python."

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    else:
        quit()

# Function that translates morse code to text

def fromorse():
    mess = input("Enter morse code")
    kod = [k for i in mess.split() for k, v in MORSE_CODE.items() if i == v]
    ciph = " ".join(kod)
    print(ciph)
    ne = input("If you want to translate text back to morse code, press 1. If you want to send the text via email, press 2. If you want to quit, press any key.")
    if ne == "1":
        print(tomorse())

    # Send the text via email (if you really want to do that...)

    elif ne == "2":
        email1 = input("Enter your email: ")
        email2 = input("Enter the receiver email: ")
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = email1
        receiver_email = email2
        password = input("Type your password and press enter: ")
        message = ciph + " This message was sent from Python."

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    else:
        quit()

# Welcome screen with options

ot = input("Translate text to morse code - press 1, Translate morse code to text - press 2, Quit - press any key")
if ot == "1":
    print(tomorse())
elif ot == "2":
    print(fromorse())
else:
    print("Goodbye.")
    quit()


