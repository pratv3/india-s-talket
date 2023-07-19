import os
from colorama import Fore as c
os.system("clear||cls")
print(f"{c.LIGHTMAGENTA_EX} TAlKNET TALKNET")
print(f"{c.LIGHTGREEN_EX}    ....MMMMMMMMMMMMMMMMMMMMM")
print(f"{c.LIGHTGREEN_EX} ..MMMMMMMMMMMMMMMMMMMMMMMMM")
print(f"{c.LIGHTGREEN_EX} MMMMMMMMMMMMMMMMMMMMMMMM")
print(f"{c.LIGHTGREEN_EX}             oOOOOOOOOOOOo")
print(f"{c.LIGHTGREEN_EX}                   OO")
print(f"{c.LIGHTGREEN_EX}                   OO"+(f"{c.LIGHTRED_EX}    00   .0"))
print(f"{c.LIGHTGREEN_EX}                   OO"+(f"{c.LIGHTRED_EX}    00  .0"))
print(f"{c.LIGHTGREEN_EX}                   OO"+(f"{c.LIGHTRED_EX}    00 .0"))
print(f"{c.LIGHTRED_EX}                         00.0")
print(f"{c.LIGHTRED_EX}                         00 .0")
print(f"{c.LIGHTRED_EX}                         00  .0")
print(f"{c.LIGHTRED_EX}                         00   .0")
print(f"{c.LIGHTRED_EX}                                      ......MMMMMMMMMMMMM")
print(f"{c.LIGHTRED_EX}                                 ....MMMMMMMMMMMMMMMMM")
print(f"{c.LIGHTRED_EX}                                .MMMMMMMMMMMMMMMMMMM")
print(f"{c.LIGHTBLUE_EX} :--Author --pratv3 and Offensive Security")
print(f"{c.RED} ---------------USE FOR EDUCATION PURPOSES-----------")
print(f"{c.GREEN}[i] WELCOME to Talknet v-2.1.0")
print(f"{c.GREEN}[i] Now you can talk to anybody in your wifi")
print(f"{c.CYAN}[i] Works on 995")
print("-"*70)
i=int(input(f"{c.LIGHTMAGENTA_EX}[?] Enter the following to next the procedure\n1:- Host \n2:- Member\n3:-Clear Logs\n[?] Enter the following:-"))
if i==1:
    os.system("clear||cls")
    import talknetHost
elif i==2 :
    os.system("cls||clear")
    import talknetMember
elif i==3:
    try:
        os.remove("talknetlogs.txt")
        print(f"{c.LIGHTGREEN_EX}[!] Log files of Host erased")
    except Exception as e:
        print(e)
        print(f"{c.LIGHTRED_EX}[!] no logfiles by Host are present")
    try:
        os.remove("talknetMlogs.txt")
        print(f"{c.LIGHTGREEN_EX}[!] Log files of Member erased")
    except Exception as e:
        print(e)
        print(f"{c.LIGHTRED_EX}[!] no logfiles by Member are present")
else:
    print(f"{c.LIGHTRED_EX}!! invalid identifier 0 from main")