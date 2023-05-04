if __name__ != "__main__":
    import socket
    import time
    import os
    import sys
    import threading
    from colorama import Fore as c
    class main:
        def __init__(self, ip, port, name):
            f = open("talknetlogs.txt", "a+")
            os.system("cls||clear")
            print(f"{c.LIGHTBLUE_EX}[i] Connecting world in unity...")
            self.ip = ip
            self.port = port
            self.name = name
            s = socket.socket(socket.AF_INET)
            try:
                s.bind((ip, port))
                s.listen(4)
            except Exception as e:
                print(e)
                print(f"{c.LIGHTRED_EX}:-Unable to create connection:-")
            con, addr = s.accept()
            try:
                print(f"{c.LIGHTYELLOW_EX}[!] Connection get at |{addr}", format(addr))
                t = time.strftime("%Y--%B--%e::--%H--%M--%S")
                f.write(f"{t}:-Host conection from | {addr}\n")
                f.close()

                def rec():
                    while True:

                        ms = input(f"{c.LIGHTYELLOW_EX}")
                        if name:
                            msg = f"{name}:-{ms}"
                            con.send(msg.encode("utf-8"))
                        else:
                            con.send(ms.encode("utf-8"))
                        if ms == "quit":
                            con.close()
                            sys.exit()


                def send():
                    while True:

                        d = con.recv(1024).decode("utf-8")
                        print(f"{c.LIGHTGREEN_EX}"+d)
                        if d == "quit":
                            print(f"{c.LIGHTMAGENTA_EX}e")
                            con.close()
                            sys.exit()
                try:
                    s=threading.Thread(target=send).start()
                    r=threading.Thread(target=rec).start()
                    
                except:
                    print(f"{c.LIGHTRED_EX}-: Connection has been closed :-")
            except Exception as e:
                con.close()
                f.close()
                print(e)
                print(f"{c.LIGHTRED_EX}[!] some errors occured")
                sys.exit()

    print(f"{c.YELLOW}shree")
    print(f"{c.LIGHTCYAN_EX}-" * 70)
    print(f"{c.LIGHTBLUE_EX}[i]Welcome to india's talknet")
    print(f"{c.LIGHTCYAN_EX}-" * 70)
    i = str(input(f"{c.MAGENTA}[?] Enter your private ip:-"))
    n = str(input(f"{c.CYAN}[?] Enter your name:-"))
    main(i, 7773, n)
else:
    print(f"[!] no abstraction layer found")
    print("[i] exited code 0")
