#Dictionary of the chatbot
#code for dictionary starts 
from math import *
import random
from PyDictionary import PyDictionary
dictionary=PyDictionary()
res="false"
def dict_bot_out():
    """ This function can print  antonyms,synonyms and meanings of the word.
    The input for this function has to be like  :meaning of list,antonym of happy,synonym of earth
    """
    str_word=input("Enter the word along with what you want to do : ")
    str_word=str_word.lower()

    try:
        typ_part=str_word[:str_word.rfind(' ')]
        word=str_word[str_word.rfind(' '):]

        if "meaning" in typ_part:
            di_meang=dictionary.meaning(word)
            for key,value in di_meang.items():
                print(key,":",random.choice(value))
                print("---------------------------------------")
        elif "synonym" in typ_part:
            print(*dictionary.synonym(word),sep=",")
            print("---------------------------------------")
        elif "antonym" or "opposite" in typ_part:
            print(*dictionary.antonym(word),sep=",")
            print("---------------------------------------")
        else:
            print("This chatbot can give you the meaning,synonym and antonym only")
            print("---------------------------------------")
        print("press enter to continue or enter quit to exit")
        res=input()
    except:
        print("Please check  spelling of the word you entered and retry..")
    if(res=="quit"):
        return "quit"
        #dictionary ends
