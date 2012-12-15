__author__ = 'holbrook'
import paramiko

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh.connect('50.1.57.9', username='oracle', password='oracle')

#cmd = '''sqlplus jgxt/hyzqhyzq@orcl <<EOF
#spool /home/oracle/livebos_tmp/msg.tmp
#@/home/oracle/livebos_tmp/PRO_CopyGDSYXMFJ_TOEMAIL.sql
##spool off
#exit
#EOF
#'''
#stdin, stdout, stderr =  ssh.exec_command(cmd)
#for line in stdout.readlines(): print line,

#stdin, stdout, stderr = ssh.exec_command('cat /home/oracle/livebos_tmp/msg.tmp')
#for line in stdout.readlines(): print line,
        

transport = paramiko.Transport(('50.1.57.9',22))
transport.connect(username='root',password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)

file = '/Users/holbrook/Documents/svnroot/dev/JGXT/src/trunk/LiveBos/Livebos/FormBuilder/hyp/hyp.htm'

localRoot = '/Users/holbrook/Documents/svnroot/dev/JGXT/'
remoteRoot = '/opt/tmp/'
ends = file[len(localRoot):]
print ends
##############create path###############
paths = ends.split('/')
curentPath = remoteRoot+'/'
for path in paths[:-1]:
    remoteFiles = sftp.listdir(curentPath)
    curentPath = curentPath+path+'/'
    if not(path in remoteFiles):
        sftp.mkdir(curentPath)
        print 'mkdir',curentPath
        

##############end of create path########
print file
print remoteRoot+ends

sftp.put(file,remoteRoot+ends)