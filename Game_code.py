
import random
import time
import sys
li=["Beautifull","heavy","little","small","jumble"] #we can add more list of strings 
flag=0
while True:
    try:
        print("Hey man are you ready to play the game? if yes enter 1 else 0 ")
        n = int(input())
        if n==1 :
            while True:
                if len(li)==0:
                    print("No strings left in stock !")
                    sys.exit()
                selected_string = random.choice(li)
                li.remove(selected_string)
                string_li = list(selected_string)
                random.shuffle(string_li)
                jumbled_str = ''.join(string_li)
                print("Here is your Jumbled letter!")
                time.sleep(2)
                print(jumbled_str)
                print("Hope you will get it right! All the best")
                hint=0
                while True:
                    if hint==0:
                        print("You have only  one hint! Enter hnt to reveal")
                    str = input("Enter here :")
                    if str=="hnt":
                        hint=1
                        k=len(selected_string)
                        print(selected_string[(k // 2):k])
                        str=input("Enter here :")
                    if str == selected_string:
                        print("Hurray! you are right")
                        time.sleep(1)
                        print("---------------------")
                        time.sleep(2)
                        print("Let's try next one")
                        flag=1
                        break
                    else:
                        print("Sorry try again")
                        continue
                if flag==1:
                    continue
        else:
            print("Exiting.",end="")
            time.sleep(1)
            print("..",end="")
            time.sleep(1)
            print("..")
            break
    except Exception as e:
            print("Something went wrong enter proper input")
