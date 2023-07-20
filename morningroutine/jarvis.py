#!/usr/bin/env python3

import subprocess
import time
import os



#Pip install first 2 libraries






'''
Windows restricted policy permanent change

Set-ExecutionPolicy Unrestricted

Set-ExecutionPolicy Restricted



Local Scope Bypass

Set-ExecutionPolicy Bypass -Scope LocalMachine



Temporary Bypass
Set-ExecutionPolicy Bypass -Scope Process



'''


#
#use the activate
#
# cd C:\Culebra\jarvisvenv\Scripts\
# .\activate
#.\python.exe ..\..\jarvis.py


#user data
#C:\Users\Jose Luis Ziccarelli\AppData\Local\Google\Chrome\User Data


#Variables
profile_name = 'Profile 1'
list_of_urls = ['https://www.scnsrc.me/',
                'https://www.notion.so/Auto-Habits-3504fb06e1aa4d4aaa93e67383371549',
                'https://www.notion.so/4d21eaa7c83a40a0b07c8e819db86adc?v=e9ccfb70b6c443fbac019833577f66bd',
                'https://ibkrcampus.com/category/traders-insight/',
                'https://attackdefense.com/members',
                'https://tomato-timer.com/']





#Commands



#Payload
def open_chrome_with_profile(profile_name, list_of_urls):
    # Set the path to your chrome browser
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # example for Windows
    profile_path = f'--profile-directory={profile_name}'
    
    # Launch Chrome with the first URL
    subprocess.Popen([chrome_path, profile_path, list_of_urls[0]])

    # Open other URLs in new tabs
    for url in list_of_urls[1:]:
        time.sleep(2)  # pause for a few seconds to allow the previous tab to load
        subprocess.Popen([chrome_path, profile_path, url])

def main():
    print("Hello, world!")
    open_chrome_with_profile(profile_name, list_of_urls)



#Ejecute el main UwU


if __name__ == "__main__":
    main()
