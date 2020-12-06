# Cache-Implementation
Implementation of Direct Mapped Cache and 4-Way Set Asocciative Cache in Python

How to Run the code? 

    Open the directory in which the code lies. There are 4 code files ExtractData.py, DM_Cache.py, SA4_Cache.py and main.py 

    The File ExtractData.py reads the data from the trace files and stores them in an array. 

    DM_Cache.py and SA4_Cache.py store the number of hits and misses in their own arrays. 

    main.py imports the data from ExtractData.py and passes them to functions of DM_Cache.py and SA4_Cache.py, it imports the hit count and miss count from the         caches and then displays the output. 

    I have used a module tabulate which displays output in tabular form. 

    This module can be installed using the command pip3 install tabulate, if not present already. 

    IMP NOTE: The output is wide and can be seen properly only on a full screen terminal. 

    Now run the code using python3 main.py on the full screen terminal. 
