savedcmd_kvcommon.o := ld -m elf_x86_64 -z noexecstack --no-warn-rwx-segments   -r -o kvcommon.o @kvcommon.mod 
