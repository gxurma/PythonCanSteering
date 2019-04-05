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


def main():

  sendElmoMsg(idX2, "PA",1,1000)
  sendElmoMsg(idX, "PA",1,-1000)
  sendElmoMsg(idY, "PA",1,-4096)
  sendElmoMsg(idZ, "PA",1,256)
  sendElmoMsg(idX2, "PX",1,100000)
  sendElmoMsg(idX2, "BG",0,00000)



if __name__ == '__main__':  # if we're running file directly and not importing it
  	main()  # run the main function
