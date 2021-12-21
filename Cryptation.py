# Cryptation.py is a Python Script used to keep all your passwords encrypted in text files, and then print them if you want.

# Made by LeCoqHardi, available on Github
# https://www.twitch.tv/lecoqhardi // https://www.twitter.com/LeCoqHardi__ // https://www.github.com/lecoqhardi


import os
import platform
import sys
import subprocess
from typing import Text
from cryptography.fernet import Fernet

save_path = 'database'
close = ""

key = b'x6-G6fyQH6edKD1ZgzBhsnNsGpRMfM0gZzNms4WB7jg='

fernet = Fernet(key)

while close != "x" :
    # This part is used to detect the OS you use and clear the console.
    OperatingSystem = platform.system()

    if OperatingSystem == "Windows":
        os.system("cls")
    else:
        os.system("clear")


    


    print("============================================================================================================")
    print("")
    print(" ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █       ██▓███ ▓██   ██▓")
    print("▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █      ▓██░  ██▒▒██  ██▒")
    print("▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒     ▓██░ ██▓▒ ▒██ ██░")
    print("▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒     ▒██▄█▓▒ ▒ ░ ▐██▓░")
    print("▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░ ██▓ ▒██▒ ░  ░ ░ ██▒▓░")
    print("░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ ")
    print("  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░      ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░▒  ░▒ ░     ▓██ ░▒░ ")
    print("░          ░░   ░ ▒ ▒ ░░  ░░         ░        ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░  ░   ░░       ▒ ▒ ░░  ")
    print("░ ░         ░     ░ ░                             ░  ░         ░      ░ ░           ░   ░           ░ ░     ")
    print("░                 ░ ░                                                                   ░           ░ ░     ")
    print("")
    print("=============================================================================================================")


#============================================ FUCTIONS PART ============================================================================
    def wait_key():
        ''' Wait for a key press on the console and return it. '''
        result = None
        if os.name == 'nt':
            import msvcrt
            result = msvcrt.getch()
        else:
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

        return result

    def addService():
        serviceadded = input("Which service do you want to add ? : ")
        completeName = os.path.join(save_path, serviceadded)
        f = open(completeName,"wb")
        #f.write("   Username : ")
        UsernameEntered = input("Username & Email & Password used on the service : (Tips : Write it U/E/P or U E P so you can copy/paste it easily !) ")
        UsernameEncrypted = fernet.encrypt(UsernameEntered.encode())
        f.write(UsernameEncrypted)
        #2f.write("\n")
        #f.write("   Email : ")
        #EmailEntered = input("Email used on the service : ")
        #EmailEncrypted = fernet.encrypt(EmailEntered.encode())
        #f.write(EmailEncrypted)
        #f.write("\n")
        #f.write("   Password : ")
        #PasswordEntered = input("Password used on the service : ")
        #PasswordEncrypted = fernet.encrypt(PasswordEntered.encode())
        #f.write(PasswordEncrypted)
        #f.write("\n")
        f.close()
    
    def showService():
        print("=========[Services saved]=========")
        os.system("ls database")
        print("==================================")
        
        serviceadded = input("Which service do you want to show ? (Pay attention to capitalization!) : ")
        if serviceadded == "":
            print("No Service entered, returning main menu...")
            print("Press any key to continue...")
            wait_key()
        else:
            completeName = os.path.join(save_path, serviceadded)
            f = open(completeName,"rb")
            TextEncrypted = f.read()
            #TextEncryptedBytes = bytes(TextEncrypted, 'utf-8')
            #print(TextEncrypted)
            #fernet.decrypt(f.read).decode
            print(fernet.decrypt(TextEncrypted).decode())
            f.close()
            print("Press any key to continue...")
            wait_key()
    
    
    def removeService():
        print("=========[Services saved]=========")
        os.system("ls database")
        print("==================================")
        serviceadded = input("Which service do you want to delete ? (Pay attention to capitalization!) : ")
        if serviceadded == "":
            print("No Service entered, returning main menu...")
            print("Press any key to continue...")
            wait_key()
        else:
            completeName = os.path.join(save_path, serviceadded)
            os.remove(completeName)
    
#===================================================================================================================================================
#============================================ APP PART =============================================================================================


    print("What do you want to do ? ")
    print("=========================")
    print("1 - Show a service")
    print("2 - Add/Edit a service")
    #print("3 - Edit a service")
    print("3 - Remove a service")
    print("4 - Close Cryptation")
    print("=========================")
    answer = input("Answer > ")
    if answer == "1":
        showService()
    if answer == "2":
        addService()
    #if answer == "3":
        #editService()
    if answer == "3":
        removeService()
    if answer == "4":
        close = "x"
    
