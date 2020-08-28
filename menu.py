import os

while(True):
    print("Hi, What can I do for you? ", end='')
    p = input()
    p = p.lower()

    if (("don't" in p) or ("do not" in p) or ("dont" in p)) and (("run" in p) or ("execute" in p) or ("open" in p)): 
        print("Ok, won't open")
    
    elif (("run" in p) or ("execute" in p) or ("open" in p)):

        if ("ide" in p):
            print("We have Android studio and Visual Studio Code")
            print("Which one to open? ",end='')
            q = input()
            q = q.lower()
            if ("visual studio" in q) or ("vs code" in q) or ("studio code" in q):
                print("Please wait. Opening Visual Studio Code.....")
                os.system("code")
            elif ("android studio" in q) or ("studio" in q):
                print("Please wait. Opening Android Studio.....")
                os.system("studio")
            else:
                print("Sorry, I am not able to help you.")

        elif ("editor" in p) or ("texteditor" in p):
            print("We have notepad and Sublime Text Editor")
            print("Which one to open? ",end='')
            r = input()
            r = r.lower()
            if ("notepad" in r):
                print("Please wait. Opening Notepad.....")
                os.system("notepad")
            elif ("sublime" in r):
                print("Please wait. Opening Sublime Text Editor.....")
                os.system("sublime_text")
            else:
                print("Sorry, I am not able to help you.")

        elif ("chrome" in p) or ("google" in p) or ("browser" in p) :
            print("Please wait. Opening Chrome.....")
            os.system("chrome")
        elif ("notepad" in p):
            print("Please wait. Opening Notepad.....")
            os.system("notepad")
        elif ("pdf" in p):
            print("Please wait. Opening FoxitPhantom.....")
            os.system("FoxitPhantomPDF")
        elif ("Skype" in p) or ("video call" in p):
            print("Please wait. Opening Skype.....")
            os.system("Skype")
        elif ("vlc" in p) or ("video player" in p):
            print("Please wait. Opening VLC.....")
            os.system("vlc")
        elif ("sublime" in p):
            print("Please wait. Opening Sublime Text Editor.....")
            os.system("sublime_text")
        elif ("android studio" in p) or ("studio" in p):
            print("Please wait. Opening Android Studio.....")
            os.system("studio")
        elif ("camera" in p):
            print("Please wait. Opening YouCam.....")
            os.system("Youcam6_webcam_camera_video")
        elif ("wordpad" in p):
            print("Please wait. Opening WordPad.....")
            os.system("wordpad")
        elif ("visual Studio" in p) or ("vs code" in p) or ("studio code" in p):
            print("Please wait. Opening Visual Studio Code.....")
            os.system("code")
        elif ("excel" in p):
            print("Please wait. Opening Excel.....")
            os.system("EXCEL")
        elif ("outlook" in p):
            print("Please wait. Opening Outlook.....")
            os.system("OUTLOOK")
        elif ("power point" in p):
            print("Please wait. Opening Outlook.....")
            os.system("POWERPNT")
        elif ("word" in p):
            print("Please wait. Opening MS Word.....")
            os.system("WINWORD")         
        else:
            print("Sorry, I don't have the application")

    elif ("thank you" in p) or ("close" in p) or ("bye" in p):
            print("Bye Bye")
            exit()
       
    else:
        print("Sorry, I am not able to help you.")



