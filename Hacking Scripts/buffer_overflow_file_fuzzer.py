#!/usr/bin/python
#Code from https://www.udemy.com/course/offensive-python-mastering-ethical-hacking-using-python/learn/lecture/8099684

import sys

if len(sys.argv) <= 2:
    print "[+] python buffer_overflow_file_fuzzer.py buffer_size filename"
    sys.exit()

buffer_size = int(sys.argv[1])
filename = sys.argv[2]
buffer_data = "A" * buffer_size
fi = open(filename,"w")
fi.write(buffer_data)
fi.close()
print "[+] Success ! , file {0} generated with {1} bytes".format(filename,buffer_size)  