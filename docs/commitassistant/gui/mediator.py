# -*- coding: utf-8 -*-

import puremvc.interfaces
import puremvc.patterns.mediator
from gui.command import *
import enum,wx
from gui.proxy import *
from gui.component import UpdateDialog, PackageDialog
import msg


class MainFrameMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    NAME = 'MainFrameMediator'

    def __init__(self, viewComponent):
        super(MainFrameMediator, self).__init__(MainFrameMediator.NAME, viewComponent)
        #init toolbar
        viewComponent.toolbar.ClearTools()
        for id in enum.TOOLS:
            (label, icon, shortHelp, longHelp, mediator) = enum.TOOLS[id]
            viewComponent.toolbar.AddLabelTool(
                id,
                label,
                wx.Bitmap(icon, wx.BITMAP_TYPE_ANY),
                wx.Bitmap(icon, wx.BITMAP_TYPE_ANY),
                wx.ITEM_NORMAL,
                shortHelp,
                longHelp
            )
            viewComponent.toolbar.Realize()

        #bind event listener
        #viewComponent.Bind(wx.EVT_CLOSE, self.onWindowClose)
        viewComponent.Bind(wx.EVT_TOOL, self.onTool)

    def onTool(self, event):
        #print event.Id
        self.facade.sendNotification(msg.APP_TOOL, event.Id)


class UpdateDlgMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    NAME = 'UpdateDlgMediator'

    def __init__(self, viewComponent):
        super(UpdateDlgMediator, self).__init__(UpdateDlgMediator.NAME, viewComponent)
        print 'UpdateDlgMediator'
        mainFrame = self.facade.retrieveMediator(MainFrameMediator.NAME).viewComponent
        dialog = self.viewComponent = UpdateDialog(mainFrame)
        dialog.Bind(wx.EVT_BUTTON, self.onBtn)

        cfgProxy = self.facade.retrieveProxy('ConfigProxy')
        cfg = cfgProxy.getSvnConfig()
        for (key, value) in cfg:
            getattr(self.viewComponent,key+'Txt').Value = value

        dialog.ShowModal()

    def onBtn(self, event):
        if(event.Id in [1, 2, 3, 4]):
            box = self.viewComponent.FindWindowById(10 + event.Id)
            #print box.Value
            pathDlg = wx.DirDialog(self.viewComponent, u'选择目录', box.Value)
            if pathDlg.ShowModal() == wx.ID_OK:
                box.Value = pathDlg.GetPath()
            pathDlg.Destroy()
            return
        if event.Id == wx.ID_OK:
            cfgProxy = self.facade.retrieveProxy('ConfigProxy')
            cfg = cfgProxy.getSvnConfig()

            for item in enum.CFG_SVN_ITEMS:
                newValue = getattr(self.viewComponent,item+'Txt').Value
                index = 0
                for (key,value) in cfg:
                    if(key==item):
                        cfg[index] = (key,newValue)
                        break
                    index = index+1
                    
            #self.facade.sendNotification(msg.SVN_STORE_CONFIG,cfg)
            cfgProxy.saveSvnConfig(cfg)
                        
            if(self.viewComponent.doUpdate.Value):
                
                print 'doUpdate'
                for item in enum.CFG_SVN_ITEMS:
                    path = getattr(self.viewComponent,item+'Txt').Value
                    
                
        event.Skip()


class PackageDlgMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):
    NAME = 'UpdateDlgMediator'

    def __init__(self, viewComponent):
        super(PackageDlgMediator, self).__init__(PackageDlgMediator.NAME, viewComponent)
        print 'UpdateDlgMediator'
        mainFrame = self.facade.retrieveMediator(MainFrameMediator.NAME).viewComponent
        dialog = self.viewComponent = PackageDialog(mainFrame)
        dialog.Bind(wx.EVT_BUTTON, self.onBtn)

        dialog.ShowModal()

    def onBtn(self, event):
        print event.Id