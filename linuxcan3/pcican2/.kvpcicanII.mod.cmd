savedcmd_kvpcicanII.mod := printf '%s\n'   PciCan2HwIf.o memQ.o | awk '!x[$$0]++ { print("./"$$0) }' > kvpcicanII.mod
