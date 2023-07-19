if __name__ != "__main__":
    import socket
    import time
    import os
    import sys
    import threading
    from colorama import Fore as c
    class main:
        def __init__(self, ip, port, name):
            f = open("talknetMlogs.txt", "a+")
            os.system("cls||clear")
            print(f"{c.YELLOW}#########################################")
            print(f"{c.YELLOW}#########################################")
            print(f"{c.YELLOW}#########################################")
            print(f"{c.WHITE}#################{c.BLUE}#####{c.WHITE}###################")
            print(f"{c.WHITE}###############{c.BLUE}#########{c.WHITE}#################")
            print(f"{c.WHITE}################{c.BLUE}######{c.WHITE}###################")
            print(f"{c.GREEN}#########################################")
            print(f"{c.GREEN}#########################################")
            print(f"{c.GREEN}#########################################")
            print(f"{c.LIGHTBLUE_EX}[i] Initated member permissions")
            print(f"{c.LIGHTGREEN_EX}[i] Connecting world in unity...")
            try:
                self.ip = ip
                self.port = port
                self.name = name
            except:
                print(f"{c.LIGHTRED_EX}:- Full information required -:")
            s = socket.socket(socket.AF_INET)
            try:
                s.connect((ip, port))
            except:
                print(f"{c.LIGHTRED_EX}:- Conection is not stable or accurate -:")
            try:
                print(f"{c.LIGHTGREEN_EX}[!] Connection get at |{ip} on {port}")
                t = time.strftime("%Y--%B--%e::--%H--%M--%S")
                f.write(f"{t}:-Member conection from | {ip} at {port}\n")
                f.close()

                def rec():
                    while True:
                        ms = input(f"{c.LIGHTYELLOW_EX}")
                        if name:
                            msg = f"{name}:-{ms}"
                            s.send(msg.encode("utf-8"))
                        elif ms == "quit":
                            s.close()
                            sys.exit()
                        elif ms=="clear":
                            os.system("clear || cls")
                        else:
                            s.send(ms.encode("utf-8"))

                def send():
                    while True:
                        d = s.recv(1024).decode("utf-8")
                        print(f"{c.LIGHTBLUE_EX}{d}")
                        if d == "quit":
                            s.close()
                            sys.exit()
                
                threading.Thread(target=send).start()
                threading.Thread(target=rec).start()
            except Exception as e:
                s.close()
                f.close()
                print(e)
                print(f"{c.LIGHTRED_EX}[!] some errors occured")
                sys.exit()

    print(f"{c.YELLOW}shree")
    print(f"{c.LIGHTCYAN_EX}-" * 70)
    print(f"{c.LIGHTBLUE_EX}[i]Welcome to india's talknet")
    print(f"{c.LIGHTCYAN_EX}-" * 70)
    i = str(input(f"{c.LIGHTMAGENTA_EX}[?] Enter your private ip to connect:-"))
    n = str(input(f"{c.LIGHTGREEN_EX}[?] Enter your name:-"))
    b=socket.gethostbyname(i)
    main(b, 995, n)
else:
    print("[!] no abstraction layer found")
    print("[i] exited code 0")
