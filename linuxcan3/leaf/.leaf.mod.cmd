savedcmd_leaf.mod := printf '%s\n'   leafHWIf.o | awk '!x[$$0]++ { print("./"$$0) }' > leaf.mod
