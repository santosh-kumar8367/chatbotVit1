import random
import emoji
from playsound import playsound
from gtts import gTTS
import os
res="false"

#This function plays random music
def music():
    print("Enjoy listening the music ",emoji.emojize(":thumbs_up:"))
    L = ["388851__enviromaniac2__piano3.mp3"]
    playsound(random.choice(L))
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res

#This function plays audio for desired story choosen
def story_telling():
    Wanted_Story = input("Choose one among these: Story for kids, Horror, Thriller, Moral and Humorous : ")
    Stories = {'Story for kids':'Story_for_kids.txt','Horror':'Horror_story.txt' ,'Thriller':'Triller.txt','Moral':'Moral_story.txt' ,'Humorous':'Humorous.txt' }
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
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res
#code ends
