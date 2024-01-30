from time import *
import random as r

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except :
            error += 1
    return error

def speed_time(time_s,time_e,userinput):
    time_dealy = time_e - time_s
    time_r = round(time_dealy, 2)
    speed = len(userinput)/ time_r
    return round(speed)
            
        
while True:
    chk = input("ready to test: yes/no:  ")
    if chk == "yes":
        test = [ "Hello", "Hi", "Welcome"]
        test1 = r.choice(test)
        print('     ***** Typing Speed ****')
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print('Speed: ',speed_time(time_1,time_2,testinput), 'word per second')
        print("Error: ", mistake(test1, testinput))
    elif chk == "no":
        print("thankyou")
        break
    else:
        print("Wrong Input")