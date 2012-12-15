#!/usr/bin/python
#-*-coding:utf-8-*-
#

__author__ = 'holbrook'

import sys,ConfigParser
from services import *
from timeFuns import *
from actions import *
from optparse import OptionParser
import config,datetime


reload(sys)
sys.setdefaultencoding('gb2312')

class CommitAssistant():
    def __init__(self):
        self.cfgInfo = ConfigParser.ConfigParser()
        self.cfgInfo.read(config.CFG_FILE)
        self.localService = LocalService()
        self.appService = None
        self.dbService = None

    
    def __run__(self,options,args):
        self.options = options
        server = {}
        server.update(self.cfgInfo.items('testServer'))
        if self.options.isOfficial:
            server.update(self.cfgInfo.items('officialServer'))

        self.localService = LocalService()
        self.appService = AppService(server)
        self.dbService = DatabaseService(server)
        
        methods = []
        for method in dir(self):
            if(callable(getattr(self,method))):
                methods.append(method)

        for cmd in args:
            if(not(cmd in methods)):
                print 'wrong command! use -h for help'
                exit()

        for cmd in args:
            fun = getattr(self,cmd)
            fun.__call__()

    def config(self):
        print 'do config'
            
    def update(self):
        print '################################ updating from svn ##################################'
        paths = self.cfgInfo.options('svnInfo')
        for pathName in paths:
            path = self.cfgInfo.get('svnInfo',pathName)
            print 'updating '+pathName+'('+path+')...............'
            self.localService.update(path)
    def commit(self):
        svnInfo = {}
        svnInfo.update(self.cfgInfo.items(('svnInfo')))
        server = {}
        server.update(self.cfgInfo.items('testServer'))
        srvName = 'test server'
        if self.options.isOfficial:
            srvName = 'official server'
            server.update(self.cfgInfo.items('officialServer'))

        print '################### commit to '+srvName +'###################################'
        
        chkDate = datetime.datetime.now() - datetime.timedelta(days=self.options.day)
        timeStr = chkDate.isoformat()[0:10] + ' 00:00:00'
        print 'check update after ', timeStr, ' :'

        boList = []
        path = self.cfgInfo.get('svnInfo','project_root')
        boList.extend(self.localService.checkUpdate(timeStr,path,ignoredFiles=config.IGNORED_XML,acceptExt='xml'))

        fileList =[]
        path = self.cfgInfo.get('svnInfo','document_root')
        fileList.extend(self.localService.checkUpdate(timeStr,path))

        path = self.cfgInfo.get('svnInfo','app_root')
        fileList.extend(self.localService.checkUpdate(timeStr,path))

        sqlList = []
        path = self.cfgInfo.get('svnInfo','sql_root')
        sqlList.extend(self.localService.checkUpdate(timeStr,path,acceptExt='sql'))

        print 'find %d business objects, %d files and %d sqls need to be commit' % (len(boList),len(fileList),len(sqlList))

        print '---------commit business objects--------------------'
        while len(boList)>0:
            file = boList.pop()
            print 'committing',file
            (code,msg) = self.appService.commitBO(server,file)

            print code,msg,'\t\t\t',file
            


        print '---------   upload files   --------------------'
        while len(fileList)>0:
            file = fileList.pop()
            code = self.appService.uploadFile(server,file,svnInfo)

        #TODO: clear tomcat work & temp directory


        print '---------commit sql objects--------------------'
        while len(sqlList)>0:
            file = sqlList.pop()
            msg = self.dbService.commitSP(file)
            print msg,file
            

if __name__=='__main__':
    usage = '''usage: %prog [options] command
command can be:
    config  :(TODO) edit the config file with an interactive interface
    test    :(TODO) test your configs
    update  :update from svn
    backup  :(TODO) backup server
    commit: commit to sample server or official server
'''

    parser = OptionParser(usage=usage)

    parser.add_option('-O','--official',help='commit to official server instead of sample server',default=False,action="store_true", dest='isOfficial')
    parser.add_option("-d", "--day", dest="day",help="day .... default=1 (yesterday)", default=1,type=int)
        
    
    cmdRrgs = ['-d 120','commit']
    #(options, args) = parser.parse_args(cmdRrgs)
    (options, args) = parser.parse_args()

    if(len(args)==0):
        print '''commit assistant for livebos
use -h form help    
'''
    else:
        myApp = CommitAssistant()
        myApp.__run__(options,args)
        


