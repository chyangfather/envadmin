#!/usr/bin/python
#-*-coding:utf-8-*-
import ConfigParser
import  urllib, os,StringIO
import config
from httplibExt import post_multipart
from timeFuns import Time2ISOString
import xml
import paramiko, commands
from models import *

__author__ = 'holbrook'


class ConfigService():
    def __init__(self,file=config.CFG_FILE):
        self.file = file
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read(file)
    def getAllSections(self):
        return self.cfg.sections()
    
    def getConfig(self,sectionName):
        return self.cfg.items(sectionName)

    def setConfig(self,sectionName,items):
        for (key,value) in items:
            self.cfg.set(sectionName,key,value)
            
        self.cfg.write(open(self.file, "w"))
        
class SvnService():
    
    @staticmethod
    def update(self,path):
        (status, output) = commands.getstatusoutput('svn up ' + path)
        return (status,output)
        

class LocalService():
    def config(self):
        print 'edit config'

    def viewConfig(self):
        print 'viewConfig'

    def update(self, path):
        (status, output) = commands.getstatusoutput('svn up ' + path)
        print output

    def checkUpdate(self, mTime, root, ignoredFiles=[],acceptExt=None):
        result = []

        for path, dirs, files in os.walk(root):
            if(path.find('.svn') >= 0):
                continue

            for f in files:
                fullPath = path + "/" + f

                doIgnore = False
                #if(root==path and f.startswith('UP')):
                #    doIgnore = True
                    
                for ignored in ignoredFiles:
                    if(fullPath.find(ignored)>=0):
                        doIgnore = True
                        break
                if(doIgnore):
                    print 'ignored file:',fullPath
                    continue

                statinfo = os.stat(fullPath)
                if (Time2ISOString(statinfo.st_mtime) < mTime):
                    continue

                if(acceptExt!=None):
                    ext = ''
                    if(len(f.split('.', -1)) > 1):
                        ext = f.split('.', -1)[1]
                    if(ext!=acceptExt):
                        continue
                result.append(fullPath)

        return result


class AppService():
    def __init__(self,server):
        transport = paramiko.Transport((server['ip'],22))
        transport.connect(username=server['sftp_user'],password=server['sftp_pwd'])
        self.sftp = paramiko.SFTPClient.from_transport(transport)
    
    def getServerObjects(self,server):     #TODO:get objects from server
        host = '50.2.62.101'
        selector = '/LiveBosStudioServer/ServiceProcessor?Action=CreateStudio&ABS_SchemeName=defaultScheme'

        fields = [
            ("userId", "admin"),
            ("password", "hy_jgxt_2011"),
            ("StudioOperateType", "1"),
            ("operate", "Get"),
            ("ABS_SchemeName", "defaultScheme"),
            ("scheme", "defaultScheme")
        ]

        files = ()#files = [('name','/wenle/a.exe','rb')]

        headers = {
            "Method": "POST",
            "EncType": "multipart/form-data",
            "Referer": ".",
            "Snapshot": "t11.inf",
            "Mode": "HTML"
        }

        resp = post_multipart(host, selector, fields, files)
        #
        str = resp.read()
        
    def commitBO(self,server,file):
        bo = LivebosObject(file)

        host=server['ip']+':'+server['app_port']
        selector = '/LiveBosStudioServer/ServiceProcessor?Action='+str(bo.actionType)+'&ABS_SchemeName='+server['app_schema']

        fields = [
            ("userId",server['app_user']),
            ("password",server['app_pwd']),
            ('scheme', server['app_schema']),
            ('operate', 'Create'),
            ('OperateType', '0'),
            ('index', '0'),
        ]
            
        ########should from xml files#####
        ignored= [
            'files',
            '__objDict__',
            '__doc__',
            '__module__',
            'actionType',
        ]
        for key in dir(bo):

            
            if key in ignored:
                continue

            value = getattr(bo,key)
            if(None==value):
                continue

            if(callable(value)):
                continue

            key1=key
            if(key=='objectId'):
                key1 = 'object-id'
            fields.append((key1,getattr(bo,key)))


#            ('actionType', bo.typeId),
#            ('object', bo.name),
#            ('object-id', bo.objectId),
#            ('describe', bo.describe),
#            ('package', bo.package)
#        ]

       # print bo.xmlStr
        commitFiles = []
        del commitFiles[:]
        for (name,url) in bo.files:
            fileStr = open(url).read()
            #if url.endswith('xml'):
            #    fileStr = fileStr.decode('gb2312')
            commitFiles.append((name,url.split('/')[-1],fileStr))

        resp = post_multipart(host, selector, fields, commitFiles)
        tmp = resp.read()
        #print tmp
        tmp = tmp.decode('gb2312')
        tmp= tmp.replace('gb2312','utf-8').encode('utf-8')
        #print tmp
        
        
        try:
            xmldoc = minidom.parseString(tmp)
            code = xmldoc.getElementsByTagName('result')[0].firstChild.data
            msg = xmldoc.getElementsByTagName('message')[0].firstChild.data
        except:
            print 'parse server message error:'
            #print tmp
            return 0,tmp
            
        #print msgXML
        #re_result = '<result>(.*?)</result>'
        #re_msg = '<message><\!\[CDATA\[(.*?)\]\]></message>'
        #print msgXML
        #code = re.compile(re_result)\
        #    .search(msgXML)\
        #    .group()[8:-9]
        #msg = re.compile(re_msg)\
        #    .search(msgXML)\
        #    .group()[18:-13]

        return code,msg

    def uploadFile(self,server,file,svnInfo):
        localRoot = svnInfo['document_root']
        remoteRoot = server['sftp_document_root']+'/'

        if(file.startswith(svnInfo['app_root'])):
            localRoot = svnInfo['app_root']
            remoteRoot = server['sftp_app_root']
        
        ends = file[len(localRoot):]

        ##############create path###############
        paths = ends.split('/')[1:-1]
        curentPath = remoteRoot
        for path in paths:
            remoteFiles = self.sftp.listdir(curentPath)
            curentPath = curentPath+'/'+path
            if not(path in remoteFiles):
                self.sftp.mkdir(curentPath)
                print 'mkdir',curentPath


        ##############end of create path########
        code = self.sftp.put(file,remoteRoot+ends)
        print code,file






class DatabaseService():
    def __init__(self,server):

        transport = paramiko.Transport((server['db_client_ip'],22))
        transport.connect(username=server['db_client_user'],password=server['db_client_pwd'])
        self.sftp = paramiko.SFTPClient.from_transport(transport)

        self.ssh = paramiko.SSHClient()

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(server['db_client_ip'], username=server['db_client_user'], password=server['db_client_pwd'])

        
    def commitSP(self,file):
        fileName = file.split('/')[-1]

        code = self.sftp.put(file,'/home/oracle/livebos_tmp/'+fileName)
        #print code,file
        cmd = '''sqlplus jgxt/hyzqhyzq@orcl <<EOF
spool /home/oracle/livebos_tmp/msg.tmp
@/home/oracle/livebos_tmp/'''+fileName+'''
spool off
exit
EOF
'''
        #print cmd
        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        stdin, stdout, stderr = self.ssh.exec_command('cat /home/oracle/livebos_tmp/msg.tmp')
        msg = ''
        for line in stdout.readlines():
            if line.startswith('SQL>'):
                continue
            if line=='\n':
                continue
            msg=msg+line

        return msg
        






