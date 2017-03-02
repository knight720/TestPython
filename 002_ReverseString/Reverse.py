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
    rs = reverse2('a(bc)defg(hi)j')
    print 'output: ', rs
    rs = reverse2('a(bc(defg)hi)j')
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

def reverse2(inS):
    print 'inS', inS

    outS = inS
    lList = []
    rList = []
    lCount = 0
    rCount = 0

    for i in range(len(inS)):
        c = inS[i]
        if c=='(':
            lList.append(i)
        elif c==')':
            rList.append(i)

        lCount = len(lList)
        rCount = len(rList)
        if lCount > 0 and (lCount == rCount):
            for ii in range(lCount):
                print 'ii',ii
                sIndex = lList[ii]+1
                eIndex = rList[ii]
                rS = reverse2(outS[sIndex:eIndex])
                sStr = outS[:sIndex-1]
                sStr = sStr if sStr is not None else ''
                eStr = outS[eIndex+1:]
                eStr = eStr if eStr is not None else ''
                print rS
                outS = sStr + rS + eStr
            return outS




    if lCount == 0:
        return outS[::-1]

    #return inS

    #print lList
    #print rList

    pass


if __name__ == '__main__':
    main()
