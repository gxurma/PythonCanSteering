savedcmd_mhydra.mod := printf '%s\n'   mhydraHWIf.o mhydraHWIf_TRP.o ioctl_handler.o | awk '!x[$$0]++ { print("./"$$0) }' > mhydra.mod
