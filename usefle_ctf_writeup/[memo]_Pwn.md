

- How to load custom library
  - set LD_LIBRARY_PATH to path that custom library is in
  - execute ldconfig

- How to use LD_PRELOAD(http://stackoverflow.com/questions/426230/what-is-the-ld-preload-trick)
  If you set LD_PRELOAD to the path of a shared object, that file will be loaded before any other library (including the C runtime, libc.so). So to run ls with your special malloc() implementation, do this:

    $ export LD_PRELOAD=/path/mylib.so
    $ ./mybin

- How to use debug symbol of libc (to see main_arena on pwndbg) 
    Make sure you've installed the debug symbols for libc:
        sudo apt-get install libc6-dbg
    And if you're on an x64 system debugging x86 code:
        sudo apt-get install libc6:i386
        sudo apt-get install libc6-dbg:i386

- How to use pwndbg
  - To see heap info
    heap
    main_arena
    bins
    fastbin

