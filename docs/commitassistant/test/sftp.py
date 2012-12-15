__author__ = 'holbrook'
import paramiko

transport = paramiko.Transport(('50.2.62.101',22))
transport.connect(username='root',password='password')
sftp = paramiko.SFTPClient.from_transport(transport)

remotepath='/root/install.log'
localpath='./a.log'
sftp.get(remotepath, localpath)



'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Very important
ssh.connect('50.2.62.101', username='root', password='password')
stdin, stdout, stderr = ssh.exec_command('ls')
print stdout.read()

ssh = paramiko.SSHClient()
known_host = os.path.expanduser("~/.ssh/known_hosts")
ssh.load_system_host_keys(known_host) # Very import
ssh.connect('10.60.2.92', username='root', password='keep_secret')
stdin, stdout, stderr = ssh.exec_command('df -h')
for line in stdout.readlines(): print line,

ssh.close() 
'''