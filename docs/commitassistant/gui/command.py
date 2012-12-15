# -*- coding: utf-8 -*-
import puremvc.patterns.command
import puremvc.interfaces
from gui.proxy import *
from gui.mediator import *
from gui.component import *


class StoreConfigCmd(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        cfgProxy = self.facade.retrieveProxy(ConfigProxy.NAME)
        cfgProxy.saveSvnConfig(note.body)
        #print a, note.body


class ToolCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        print note.body
        (label, icon, shortHelp, longHelp, Mediator) = enum.TOOLS[note.body]
        mediator = Mediator(None)

        self.facade.registerMediator(mediator)

        #self.facade.registerMediator(UpdateDlgMediator(None))


class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self, note):
        print '#####app startup command'

        ###### 1st proxy, 2nd mediator!!  bcz mediator may call proxy  ######
        self.facade.registerProxy(ConfigProxy())
        self.facade.registerProxy(ViewProxy())
        self.facade.registerProxy(ResourceProxy())


        #self.facade.registerProxy(proxy.RoleProxy())
        #self.facade.registerMediator(gui.mediator.UserFormMediator(mainPanel.userForm))
        #self.facade.registerMediator(gui.mediator.UserListMediator(mainPanel.userList))
        #self.facade.registerMediator(gui.mediator.RolePanelMediator(mainPanel.rolePanel))

        print 'start app mainloop'
        #        wxApp.MainLoop()
        app = MyApp(0)
        #wx.InitAllImageHandlers()

        self.facade.registerMediator(MainFrameMediator(app.TopWindow))
        self.facade.registerCommand(msg.APP_TOOL, ToolCommand)
        
        app.MainLoop()



        
        
