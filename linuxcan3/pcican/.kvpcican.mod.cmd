savedcmd_kvpcican.mod := printf '%s\n'   PciCanHwIf.o dallas.o | awk '!x[$$0]++ { print("./"$$0) }' > kvpcican.mod
