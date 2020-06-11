#!/usr/bin/env python

import sys
import os
import urllib.parse
import urllib.request
import subprocess

def downloadPhotoFromLink(link, fileName):

    insta_url = link
    photo_url = insta_url+"media/?size=l"
    urllib.request.urlretrieve(photo_url, fileName)
    print("A photo from Instgram URL is saved.")

def sendPhotoToPrintWithFilename(fileName):

    print_or_not = input("Do you want to print it out? (Y/N) :")

    if print_or_not == ('Y' or 'y' or 'yes' or 'Yes' or 'YES'):
        subprocess.call(["lp", fileName])

    else:
        print("Program is Ended.")

if len(sys.argv) != 3:
    print("Enter your input value: [print.py] [Instagram URL] [File Name]")
    sys.exit()

else:
    imageLink = sys.argv[1]
    fileName = sys.argv[2] + '.jpeg'

    if not os.path.exists(fileName):
        downloadPhotoFromLink(imageLink, fileName)
        sendPhotoToPrintWithFilename(fileName) 

    else:
        print(fileName, " is already existed.")
        sendPhotoToPrintWithFilename(fileName)        
        sys.exit()

