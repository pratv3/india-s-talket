if __name__!="__main__":
    import socket
    import time
    import os
    import sys
    import threading
    class main():
        def __init__(self,ip,port,name):
            f=open("talknetMlogs.txt","a+")
            os.system("cls||clear")
            print("[i] Connecting world in unity...")
            try:
                self.ip=ip
                self.port=port
                self.name=name
                s=socket.socket(socket.AF_INET)
                s.connect((ip,port))
                print(f"[!] Connection get at |{ip} on {port}")
                t=time.strftime("%Y--%B--%e::--%H--%M--%S")
                f.write(f"{t}:-Member conection from | {ip} at {port}\n")
                f.close()
                def rec():
                    while True:
                        ms=input("")
                        msg=(f"{name}:-{ms}")
                        s.send(msg.encode("utf-8"))
                        if ms=="quit":
                            s.close()
                            sys.exit()
                def send():
                    while True:
                        d=s.recv(1024).decode("utf-8")
                        print(d)
                        if d=="quit":
                            s.close()
                            sys.exit()
                threading.Thread(target=send).start()
                threading.Thread(target=rec).start()
            except Exception as e:
                s.close()
                f.close()
                print(e)
                print("[!] some errors occured")
                sys.exit()


    print("shree")
    print("-"*70)
    print("[i]Welcome to india's talknet")
    print("-"*70)
    i=str(input("[?] Enter your private ip to connect:-"))
    n=str(input("[?] Enter your name:-"))
    main(i,7773,n)
else:
    print("[!] no abstraction layer found")
    print("[i] exited code 0")



