#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     02/03/2017
# Copyright:   (c) User 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #abcdefghij
    rs = reverse('a(bc)defg(hi)j')
    print 'output: ', rs
    rs = reverse('a(bc(defg)hi)j')
    print 'output: ', rs
    pass

def reverse(s):
    print s
    si = s.find('(')
    print "si ",si

    if (si>0):
        rs = reverse(s[si+1:])
        return s[:si] + rs
    else:
        ei = s.find(')')
        print "ei ",ei
        if (ei > 0):
            rs = reverse(s[si+1:ei])
            return rs + s[ei+1:]
        else:
            rs = s[::-1]
            print rs
            return rs
    pass



if __name__ == '__main__':
    main()
