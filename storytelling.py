import random
import emoji
from playsound import playsound
from gtts import gTTS
import os
res="false"
def music():
    """ This function plays random music"""
    print("Enjoy listening the music ",emoji.emojize(":thumbs_up:"))
    L = ["192197__biblicalbricksproductions__a-major-guitar.wav","388851__enviromaniac2__piano3.mpeg"]
    playsound(random.choice(L))
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res


def story_telling():
    """ This functions plays audio of the selected story"""
    Wanted_Story = input("Choose one among these: Story for kids, Horror: ")
    Stories = {'Story for kids':'Story_for_kids.txt','Thriller':'Triller.txt' }
    try:
        if Wanted_Story in Stories:
            story = Stories[Wanted_Story]
            fh = open(story, "r", encoding="utf8")
            my_text = fh.read().replace('\n',' ')
            output = gTTS(text = my_text, lang = 'en', slow = False)
            output.save("output.mp3")
            fh.close()
            os.system("start output.mp3")
            print("Story was completed "+emoji.emojize(":smiling_face_with_smiling_eyes:"))
        else:
            print(emoji.emojize(":pensive_face:")+"\nPlease choose one from the above list only")
    except Exception as e:
        print("Select only above mentioned stories")
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res
