#!/usr/bin/python
#-*-coding:utf-8-*-
import ConfigParser,sys
from services import *
from models import *
__author__ = 'holbrook'

reload(sys)
sys.setdefaultencoding('gb2312')

cfgInfo = ConfigParser.ConfigParser()
cfgInfo.read('../conf/config.conf')
server = {}
server.update(cfgInfo.items('testServer'))
appService = AppService(server)

ROOT='/Users/holbrook/Documents/svnroot/dev/JGXT/src/trunk/JGXT/'

files = [
    #ROOT+'scope-factor.xml',
    #ROOT+'functionPermission.xml',
    #ROOT+'script-variable.xml',
    #ROOT+'meta-column.xml',
    #ROOT+'services.xml',
    #ROOT+'portlet-defines.xml',
    #ROOT+'mobile.xml',
    #ROOT+'resource.xml',
    #ROOT+'sysparam.xml',
    #ROOT+'dictionary.xml',
    #ROOT+'创新投资/项目管理/项目退出/WF_XM_TCSQ.xml',
    #ROOT+'固定收益/预算和费用分摊/vGDSY_WFTFYGL.xml',
    ROOT+'SYSTEM.xml',
    ROOT+'UP131.xml',
    ROOT+'UP134.xml',
    ROOT+'UP135.xml',
    ROOT+'UP136.xml',
    ROOT+'UP137.xml',
    ROOT+'UP138.xml',
    ROOT+'UP139.xml',
    ROOT+'UP140.xml',
    ROOT+'UP144.xml',
    ROOT+'UP172.xml',
    ROOT+'UP193.xml',
    ROOT+'UP198.xml',

]

for file in files:
    #bo = LivebosObject(file)
    #print bo

    (code,msg) = appService.commitBO(server,file)
    print code,msg,'\t\t\t',file

