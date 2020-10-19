#import math library
from math import * 
res="false"
#This function  evaluates an expression
def cal_exp():
   
    exp_num=input("Enter expression : ")
    try:
        print("Result of",exp_num,"=",eval(exp_num))  #eval functions an expression 
    except Exception as e:
        print(str(e))
    print("press enter to continue or enter quit to stop")
    res=input()
    if(res=="quit"):
        return res
    
    
