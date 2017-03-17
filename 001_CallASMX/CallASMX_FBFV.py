# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# Name:        CallASMX
# Purpose:
#
# Author:      User
#
# Created:     16/02/2017
# Copyright:   (c) User 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# https://fedorahosted.org/suds/
from suds.client import Client

def main():
    print 'start...'
    #print u'中文'
    call()
    print 'finish...'
    pass

def call():
    #url = 'http://www.webservicex.net/WeatherForecast.asmx?WSDL'
    url = 'http://123.51.211.225/ForestryDBService/DBTools.asmx?wsdl'
    client = Client(url)

    list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]
    print list_of_methods

    result = client.service.GetUserTableFinalFixDate()
    rBig5 = result.encode('big5')
    print rBig5

    result = client.service.GetUserDataIDs()
    rBig5 = result.encode('big5')
    print rBig5

    result = client.service.GetUserDataByIndex(12)
    rBig5 = result.encode('big5')
    print rBig5

    result = client.service.GetUserFixDateByIndex(12)
    rBig5 = result.encode('big5')
    print rBig5

    result = client.service.GetDeptDataIDs()
    rBig5 = result.encode('big5')
    print rBig5


    result = client.service.GetDeptDataByIndex(02)
    rBig5 = result.encode('big5')
    print rBig5

    pass



if __name__ == '__main__':
    main()
