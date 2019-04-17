#!/usr/bin/env python3
import socket
import re
import time

idX = 0x16
idY = 0x1c
idZ = 0x39
idC = 0x18
idX2 = 0x4e

idTx = 0x300
idRx = 0x280

def v(a,n):
    a1=(a>>(8*n))&255
    return a1


def sendElmoMsg(axeId, command, index, value):
    print ("%x %s %d %d" % (axeId, command, index, value))
    b=bytearray(command,"ascii")
    print ("%x %x %x %02x %02x %02x %02x %02x %02x" % (idTx+axeId, b[0],b[1], index, 0, v(value,0), v(value,1), v(value,2), v(value,3)))


class Color:
   Red = '\033[91m'
   red = '\033[31m'
   Green = '\033[92m'
   green = '\033[32m'
   Yellow = '\033[93m'
   yellow = '\033[33m'
   Blue = '\033[94m'
   blue = '\033[34m'
   Magenta = '\033[95m'
   magenta = '\033[35m'
   Cyan = '\033[96m'
   cyan = '\033[36m'
   Bold = '\033[1m'
   Underline = '\033[4m'
   end = '\033[0m'

def analyseData(data):
    if data:
        d=data.decode().split(';')[0]  # strip the comment, if any
        if d[0]=='@':
            print(Color.yellow+d[1:].encode()+Color.end)
        else:
            print(Color.Green+d+Color.end)
            m = re.search("(M)([-0-9.]+)", d, re.I)
            g = re.search("(G)([-0-9.]+)", d, re.I)
            x = re.search('(X)([-0-9.]+)', d, re.I)
            y = re.search('(Y)([-0-9.]+)', d, re.I)
            z = re.search('(Z)([-0-9.]+)', d, re.I)
            c = re.search('(C)([-0-9.]+)', d, re.I)
            f = re.search('(F)([-0-9.]+)', d, re.I)
            print(Color.Green+repr(g)+Color.end)
            if m:
               if m[2] == '400':
                  time.sleep(0.25)
                  print(Color.Green+'Wait!!!'+Color.end)
               if m[2] == '17':
                  print(Color.Green+'drive1'+Color.end)
               return
            if g:
               if g[2] == '28':
                  print(Color.Green+'Homing sent to drive'+Color.end)
                  time.sleep(0.5)
               if x:
                   sendElmoMsg(idX, "PA", 0, int(float(x[2])*200.0+.5))
                   sendElmoMsg(idX, "BG", 0,0)
               if y:
                   sendElmoMsg(idY, "PA", 0, int(float(y[2])*200.0+.5))
                   sendElmoMsg(idY, "BG", 0,0)
               if z:
                   sendElmoMsg(idZ, "PA", 0, int(float(z[2])*2000.0+.5))
                   sendElmoMsg(idZ, "BG", 0,0)
               if c:
                   sendElmoMsg(idC, "PA", 0, int(float(c[2])*200.0+.5))
                   sendElmoMsg(idC, "BG", 0,0)
               if f:
                   print(Color.Green+f[0]+'\n\r'+f[1]+'\n\r'+f[2]+Color.end)


def main():

    print("started...")
    # sendElmoMsg(idX2, "PA",1,1000)
    # sendElmoMsg(idX, "PA",1,-1000)
    # sendElmoMsg(idY, "PA",1,-4096)
    # sendElmoMsg(idZ, "PA",1,256)
    # sendElmoMsg(idX2, "PX",1,100000)
    # sendElmoMsg(idX2, "BG",0,-(2048-256))
    # sendElmoMsg(idX2, "BG",0,-900)

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    print(data)
                    if not data:
                        break
                        print("got hangup message")
                    analyseData(data)
                    time.sleep(0.5)
                    conn.sendall(b'ok\r\n')  # Hope it won't block
                    print(Color.Magenta+'wroteback ok to tcp'+Color.end)


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
