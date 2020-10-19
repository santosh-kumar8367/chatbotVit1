import random
from gtts import gTTS
import os
import emoji
from math import sin,cos,tan,factorial,fabs
from datetime import datetime

def intitiating_bot():
    intro=["\nHey good to see you.. "+emoji.emojize(":star-struck:")+" I am chatbot  \n","Hello user hope you are doing well.. "+emoji.emojize(":grinning_face_with_big_eyes:")+" I am chat bot   \n "]
    return random.choice(intro)

def asking_info():

    return input()

def greeting_user():
    current_time = datetime.now()
    current_wish = "Good morning"
    if(current_time.hour>12 and current_time.hour<18):
        current_wish="Good afternoon ! "
    elif(current_time.hour<12):
        current_wish="Good morning ! "
    elif (current_time.hour >18 and current_time.hour <=21):
        current_wish = "Good evening ! "
    elif(current_time.hour<12):
        current_wish="Hey it is too late ! "
    return current_wish+emoji.emojize(":slightly_smiling_face:")

def text_to_speech():
    mytext = input("enter the word that you want it's spell : ")
    if(mytext != "quit"):
        language = "en"
        output = gTTS(text = mytext,lang=language,slow=True)
        output.save("output.mp3")
        os.system("start output.mp3")
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res

def bot():
    print(intitiating_bot())
    print("Could I know your name please "+emoji.emojize(":smiling_face_with_smiling_eyes:"))
    name=asking_info() 
    print("\n")
    wish= greeting_user()
    print(wish, name)
    print()
    res="notquit"
    while(res!="wholeexit"):
        print("Tasks can be done by me "+emoji.emojize(":smiling_face_with_halo:"))
        print("Enter 1 : calculations")
        print("Enter 2 : Dictionary ")
        print("Enter 3 : music")
        print("Enter 4 : storytelling")
        print("Enter 5 : How to pronounce a word ")
        print("Enter 6 : To exit from chatbot\n")
        option = int(input("Enter your choice : "))
        pro="notquit"
        if(option == 1):
            from calculations import cal_exp
            res="false"
            while(res!="quit"):
                res= cal_exp()
                

        elif(option == 2):
            from calcdic import dict_bot_out
            res="false"
            while(res!="quit"):
                res=dict_bot_out()
            
            

        elif(option == 3):
            from storytelling import music
            res="false"
            while(res!="quit"):
                res=music()
        
        elif(option == 4):
            from storytelling import story_telling
            res="false"
            while(res!="quit"):
                res=story_telling()

        elif(option == 5):
            res="false"
            while(res!="quit"):
                res=text_to_speech()
        elif(option == 6):
            print("\nThanks for chatting... "+emoji.emojize(":grinning_face:")+" Hope you have a great time "+emoji.emojize(":smiling_face_with_smiling_eyes:")+"\n")
            break
        else:
            print("Please enter valid option.. ",emoji.emojize(":disappointed_face:")+"\n")

            
            
bot()