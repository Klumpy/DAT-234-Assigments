

import sys
import getopt
import os
import time
import string





def output_passwordlist(output_fp):
    f = open(output_fp, "w")

    ascii = string.printable
    for i in ascii:
        f.write("{}\n".format(i))

    f.close()





if __name__ == "__main__":

    output_fp = "ascii_list.txt"
    try:
        output_passwordlist(output_fp)
    except Exception as e:
        print "Oh no, something went wrong."
        print(e)
        sys.exit(1)




