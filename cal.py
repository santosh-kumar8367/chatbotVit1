from math import *
res="false"
print("Enter quit to edit the task")
while(res!="quit"):
    res=cal_exp()
    def cal_exp():
        """ This function  evaluates an expression"""
        exp_num=input("Enter expression : ")
        try:
            print("Result of",exp_num,"=",eval(exp_num))
        except Exception as e:
            print(str(e))
        print("press enter to continue or enter quit to stop")
        res=input()
        if(res=="quit"):
          return res
