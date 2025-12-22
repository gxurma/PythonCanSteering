savedcmd_usbcanII.mod := printf '%s\n'   usbcanHWIf.o | awk '!x[$$0]++ { print("./"$$0) }' > usbcanII.mod
