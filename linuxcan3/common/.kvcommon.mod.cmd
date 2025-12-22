savedcmd_kvcommon.mod := printf '%s\n'   VCanOsIf.o objbuf.o queue.o util.o softsync.o capabilities.o dlc.o ticks.o | awk '!x[$$0]++ { print("./"$$0) }' > kvcommon.mod
