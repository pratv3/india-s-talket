import os
os.system("clear||cls")
print("By Remembering GOD")
print("-"*70)
print("[i] WELCOME to india's talknet")
print("[i] Now you can talk to anybody in your wifi")
print("[i] Works on 7773")
print("-"*70)
i=int(input("[?] Enter the following to next the procedure\n1:- Host \n2:- Member\n3:-Clear Logs\n[?] Enter the following:-"))
if i==1:
    os.system("clear||cls")
    import talknetHost
elif i==2 :
    os.system("cls||clear")
    import talknetMember
elif i==3:
    try:
        os.remove("talknetMlogs.txt")
        os.remove("talknetlogs.txt")
        print("[!] Log files erased")
    except Exception as e:
        print(e)
        print("[!] no logfiles are present")
else:
    print("!! invalid identifier 0 from main")