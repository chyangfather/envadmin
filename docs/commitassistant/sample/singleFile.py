from httplibExt import post_multipart
import sys
__author__ = 'holbrook'


reload(sys)
sys.setdefaultencoding('gb2312')

host = '50.1.57.22'
selector = '/LiveBosStudioServer/ServiceProcessor?Action=CreateScopeFactor&ABS_SchemeName=defaultScheme'

fields = [
            ("userId",'admin'),
            ("password",'000000'),
            ('scheme', 'defaultScheme'),
            ('operate', 'Create'),
            ('OperateType', '0'),
            ('index', '0'),
        ]

        

files = [
    ('scope-factor.xml','scope-factor.xml',open('./scope-factor.xml').read()),
]

resp = post_multipart(host, selector, fields, files)
#
str = resp.read().decode('gb2312')
print str 
  