
## RS-AX6-PY
wrapper around the AX6 C library
Testing on windows 11 pro (python 64bit, x64 arch)
(previous worked on macOS - 12.7 using .so)

NOTE: 
.h file is required to be in c directory (to use _generate.sh)
can include the .h from where it is located if _generate is modified

### generate the wrapper
ctypesgen is installed via pip
ctypesgen -a -l ../../src/libomapi.so ../../include/omapi.h -o pylibomapi.py 

### mac
ctypesgen -a -l libomapi.so omapi.h -o pylibomapi_wrapper.py

### windows
ctypesgen -a -l libomapi.dll omapi.h -o pylibomapi_win_wrapper.py

generate.cmd will also generate the wrapper on windows

python test.py - runs a mimic of test.c
python record.py - runs a mimic of record.c (wip)



