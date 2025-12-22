savedcmd_kvvirtualcan.mod := printf '%s\n'   virtualcan.o | awk '!x[$$0]++ { print("./"$$0) }' > kvvirtualcan.mod
