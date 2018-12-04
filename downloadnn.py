# -*- coding: utf-8 -*-
# This script demonstrates using pyautogui for simple web automation
# In this case we are downloading a file from a website using pyautogui
# To mimic mouse control.

import pyautogui
import time
import os
import subprocess
import sys

#Open Firefox
subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe'])
#Allow time for FF to open
time.sleep(10)
#Move to the menu bar and click the site
pyautogui.moveTo(50, 130)
pyautogui.click()
time.sleep(10)
#Select the document
pyautogui.moveTo(1772, 767)
time.sleep(2)
#scroll up on the menu
pyautogui.scroll(-700)
time.sleep(10)
pyautogui.click()
#Confirm
time.sleep(10)
pyautogui.moveTo(1775, 426)
pyautogui.click()
#Move mouse and allow it time to download
time.sleep(30)
pyautogui.moveTo(363, 23)
pyautogui.click()
time.sleep(3600)
#Close Firefox
pyautogui.moveTo(1890,20)
pyautogui.click()
#Runa  batch file to move the files to the proper drive and directory because it's a pain in python
batchfile = "E:\\scripts\\movenn.bat"
os.system( "%s" % batchfile)
