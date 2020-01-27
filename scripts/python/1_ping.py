import os


class PingIP:
    '2 functions: One will ping localhost when object is created, other will ping an IP range.'
    
    def __init__(self):
        os.system("ping -c 1 localhost")
 
    def ip_range(self, address):
        s = address.split('.')
        try:
            os.system("fping -a -q -g {}.{}.{}.0 {}.{}.{}.255".format(s[0], s[1], s[2], s[0], s[1], s[2]))
        except TypeError:
            print "wrong input"
        except OSError:
            print "OS Error"
        else:
            print "Input correct, will now ping range... "


myClass = PingIP()
myClass.ip_range("10.0.0.120")

