# -*- coding: utf-8 -*-
import puremvc.patterns.proxy
import enum, vo
from services import ConfigService, SvnService

class SVNProxy(puremvc.patterns.proxy.Proxy):
    NAME = "SVNProxy"
    def __init__(self):
        super(SVNProxy, self).__init__(SVNProxy.NAME)
        self.cfgService = ConfigService()
    def update(self,path):
        return SvnService.update(path)   #(status,output) 

        
class ConfigProxy(puremvc.patterns.proxy.Proxy):
    NAME = "ConfigProxy"

    def __init__(self):
        super(ConfigProxy, self).__init__(ConfigProxy.NAME)
        self.cfgService = ConfigService()

    def getSvnConfig(self):
        return self.cfgService.getConfig(enum.CFG_SVN_SECTION)

    def saveSvnConfig(self,cfg):
        self.cfgService.setConfig(enum.CFG_SVN_SECTION,cfg)

class ViewProxy(puremvc.patterns.proxy.Proxy):
    NAME = "ViewProxy"
    #vo :(name, type, children)

    def __init__(self):
        super(ViewProxy, self).__init__(ViewProxy.NAME)

    def getViews(self):
        views = [
                {'name': 'devEnv', 'value': 'abc'},
                {'name': 'testEnv', 'value': 'def'},
                {'name': 'officalEnv', 'value': 'ghi'},
        ]

        return views


class ResourceProxy(puremvc.patterns.proxy.Proxy):
    NAME = "ResourceProxy"
    #vo :(name, type, children)

    def __init__(self):
        super(ResourceProxy, self).__init__(ResourceProxy.NAME, [])

    def createCategory(self, parent=None):
        category = ResCategory()
        category.name = 'new category'
        category.parent = parent
        category.save()
        return category

    def createResource(self, type=None):
        resource = Resource()
        resource.name = 'new resource'
        resource.type = type
        resource.save()

        return resource

    def getRootCategories(self):
        queryset = ResCategory.objects.filter(parent=None)
        return list(queryset)


class UserProxy(puremvc.patterns.proxy.Proxy):
    NAME = "UserProxy"

    def __init__(self):
        super(UserProxy, self).__init__(UserProxy.NAME, [])
        self.data = []
        self.addItem(vo.UserVO('lstooge', 'Larry', 'Stooge', "larry@stooges.com", 'ijk456', enum.DEPT_ACCT))
        self.addItem(vo.UserVO('cstooge', 'Curly', 'Stooge', "curly@stooges.com", 'xyz987', enum.DEPT_SALES))
        self.addItem(vo.UserVO('mstooge', 'Moe', 'Stooge', "moe@stooges.com", 'abc123', enum.DEPT_PLANT))

    def getUsers(self):
        return self.data

    def addItem(self, item):
        self.data.append(item)

    def updateItem(self, user):
        for i in range(0, len(self.data)):
            if self.data[i].username == user.username:
                self.data[i] = user

    def deleteItem(self, user):
        for i in range(0, len(self.data)):
            if self.data[i].username == user.username:
                del self.data[i]