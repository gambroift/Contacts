# Contacts
### This repo contains code for importing contacts in your phone from telegram 

During a relaxing sunday evening I open WhatsApp and I discovered that all my contacts were deleted.
I tried to recover them from my Google account but nothing, probably I was out of sync. Luckily telegram had stored my contacts information. 

In this repo I try to explain how to recover your contacts from Telegram and import them in your phone, I hope it can be useful to someone.

## Step 1: Download Telegram contact list
### 1.1 Download and install Telegram App in your PC
Windows https://telegram.org/dl/desktop/win64
macOs https://telegram.org/dl/desktop/mac
### 1.2 Go to Telegram settings and click Advanced
![image](https://github.com/user-attachments/assets/dcbe21f8-7f5a-4f3e-b7fa-3bf279b2a24f)
### 1.3 Scroll down and export Telegram data
![image](https://github.com/user-attachments/assets/5b3cebea-0595-496b-be2e-9a40e5bb608a)
### 1.4 Select Contacts list and Export
![image](https://github.com/user-attachments/assets/9d43fd51-c272-422c-ad05-7b2b1071c06e)

This will download an html file containing your contacts' data. Now we have to convert it into a csv file which can be uploade in Google Contacts (https://contacts.google.com/).

## Step 2: Read the html file and retrieve contacs information

Execute the python script contacts.py (loaded in the repo) in the same folder with the Telegram html file and the pre-set csv file. 
#### Note: it is important to use the pre-set csv file because google contacs recognize the coloumns' name and store data in the correct way.
If neessary you can download python from https://www.python.org/downloads/. A user giude can be found at https://wiki.python.org/moin/BeginnersGuide.
The script will output your contacts' data in a csv file storing: Name, Surname and Phone Number (you can modify the script to store also the email or other data if necessary).

## Step 3 Import the csv file into Google Contacts
Go to Google contacts https://contacts.google.com/ and click on Import, then choose your csv file.

## Step 4 Activate syncing on your phone 
In few minutes syncing will transfer Google Contacts in your phone and voilà.
