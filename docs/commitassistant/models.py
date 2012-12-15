#!/usr/bin/python
#-*-coding:utf-8-*-
import cStringIO
import codecs
import re
from xml.dom import minidom
from httplibExt import *
import codecs

class LivebosObject():
    object = None
    type = None
    actionType = None
    objectId = None
    version=None
    modifyDate=None   #"2011.04.20 14:25:30"
    createDate=None    #"2011.04.20 14:22:30"
    creator=None
    modifier=None
    package=None
    describe=None

    #object=None         #for workflow
    
    files=[]        #(name,url) in it


    __objDict__ = {
        'functionPermission.xml':{              #功能权限树
            #'type':u'功能权限树',
            'actionType':'-16',
            'package':'U1NP'
        },
        'scope-factor.xml':{                    #数据权限分区
            #'type': u'数据权限分区',
            'actionType':'CreateScopeFactor'
        },
        'meta-column.xml':{                     #元数据
            #'type': u'元数据',
            'object':'',
            'actionType':'CreateMetaColumn'
        },
        'script-variable.xml':{                 #系统变量
            #'type': u'系统变量',
            'actionType':'CreateScriptVeriable'
        },

        'services.xml':{                        #系统服务
            #'type': u'系统服务',
            'actionType':'-9'
        },
        'portlet-defines.xml':{                 #Portlet配置信息
            #'type': u'Portlet配置信息',
            'actionType':'-14'
        },
        'mobile.xml':{
            #'type': u'手机界面配置',
            'actionType':'-13'
        },

        'resource.xml':{                 
            #'type': u'数据源',
            'actionType':'-10'
        },
        'sysparam.xml':{
            #'type': u'系统参数',
            'actionType':'CreateSysParam'
        },
        'dictionary.xml':{
            #'type': u'数据字典',
            'object':'',
            'actionType':'CreateDict'
        },

        #'SYSTEM.xml':{                 #系统默认方案 TODO:2 ge wen jian 
        #    'type': u'系统默认方案',
        #    'typeId':'-9'
        #},
    }
    

    def __init__(self, file=None):
        if(file!=None):
            self.update(file)
            


    def __createBusinessObject__(self,file):        #其他对象
        
        f = codecs.open(file)
        f.readline()
        str = f.read().decode('gb2312')
        f.close()

        xmlStr = str.encode('utf-8')
        #print xmlStr
        
        xmldoc = minidom.parseString(xmlStr)

        root = xmldoc.documentElement

        #self.type = root.nodeName
        self.actionType = root.attributes['type'].value.encode('gb2312')
        self.object = root.attributes['name'].value.encode('gb2312')
        self.objectId = root.attributes['object-id'].value.encode('gb2312')
        #self.version = root.attributes['name'].value.encode('gb2312')
        #self.modifyDate = root.attributes['modify-date'].value.encode('gb2312')
        #self.createDate = root.attributes['create-date'].value.encode('gb2312')
        #self.creator = root.attributes['creator'].value.encode('gb2312')
        #self.modifier = root.attributes['modifier'].value.encode('gb2312')
        self.package = root.attributes['package'].value.encode('gb2312')
        self.describe = root.childNodes[1].firstChild.nodeValue.encode('gb2312')


        
    def update(self,file):
        del self.files[:]
        fileName = file.split('/')[-1]
        self.files.append((fileName,file))
        
        if fileName in self.__objDict__:                        #system object
            self.__dict__.update(self.__objDict__[fileName])
            return

        
        if fileName.startswith('WF_'):                          #workfolw
            
            self.actionType = '6'
            self.object = fileName[0:-4]
            
            
            self.files.append(('workflowdes',file))
            self.files.append(('layout',file[0:-4]+'_layout.xml'))
            self.files.append(('image',file[0:-4]+'.jpeg'))
            
            return

        if fileName=='SYSTEM.xml' or fileName.startswith('UP'): #
            #self.files.append((fileName[0:-4],file))

            #find menu file
            f = open(file)
            f.readline()
            str = f.read().decode('gb2312')
            
            xmldoc = minidom.parseString(str.encode('utf-8'))
            fileNodes = xmldoc.getElementsByTagName('file')
            if len(fileNodes)>0:
                menuFile = fileNodes[0].attributes['href'].value
                menuFile = file[0:-len(fileName)]+menuFile
                self.files.append(('menu',menuFile.encode("ascii")))


            self.actionType = '-12'
            self.object = fileName[0:-4]
            
            return


        self.__createBusinessObject__(file)                     #其他对象


    

        
        
        