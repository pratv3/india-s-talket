if __name__!="__main__":
    import socket
    import time
    import os
    import sys
    import threading
    class main():
        def __init__(self,ip,port,name):
            f=open("talknetlogs.txt","a+")
            os.system("cls||clear")
            print("[i] Connecting world in unity...")
            try:
                self.ip=ip
                self.port=port
                self.name=name
                s=socket.socket(socket.AF_INET)
                s.bind((ip,port))
                s.listen(4)
                con,addr=s.accept()
                print("[!] Connection get at |{addr}",format(addr))
                t=time.strftime("%Y--%B--%e::--%H--%M--%S")
                f.write(f"{t}:-Host conection from | {addr}\n")
                f.close()
                def rec():
                    while True:
                        
                        ms=input("")
                        msg=(f"{name}:-{ms}")
                        con.send(msg.encode("utf-8"))
                        if ms == "quit":
                            con.close()
                            sys.exit()
                def send():
                    while True:
                        
                        d=con.recv(1024).decode("utf-8")
                        print(d)
                        if  d =="quit":
                            print("e")
                            con.close()
                            sys.exit()
                threading.Thread(target=send).start()
                threading.Thread(target=rec).start()
            except Exception as e:
                con.close()
                f.close()
                print(e)
                print("[!] some errors occured")
                sys.exit()


    print("shree")
    print("-"*70)
    print("[i]Welcome to india's talknet")
    print("-"*70)
    i=str(input("[?] Enter your private ip:-"))
    n=str(input("[?] Enter your name:-"))
    main(i,7773,n)
else:
    print("[!] no abstraction layer found")
    print("[i] exited code 0")

