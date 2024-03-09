from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

while True:
    ck = input("ready to test : Y/N : ").upper()
    if (ck == "Y"):
        test = ["my name is vishal","this paragraph is a 2'nd string","this paragraph is a 3'th string","this paragraph is a 4'th string'"]
        test1 = r.choice(test)
        print("           *****typing speed*****          ")
        print(test1+"\n\n")
        time_1 = time()
        test_input = input("Enter : ")
        time_2 = time()

        print('Speed : ',speed_time(time_1, time_2,test_input),"w/sec")
        print('Error : ',mistake(test1,test_input))
    elif (ck=="N"):
        print("thank you")
        break
    else:
        print("please enter currect input")


