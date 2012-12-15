# -*- coding: utf-8 -*-
import sys,time
import puremvc
from gui.command import *


class AppFacade(puremvc.patterns.facade.Facade):
    NEW_USER          = "newUser"
    DELETE_USER       = "deleteUser"
    CANCEL_SELECTED   = "cancelSelected"

    USER_SELECTED     = "userSelected"
    USER_ADDED        = "userAdded"
    USER_UPDATED      = "userUpdated"
    USER_DELETED      = "userDeleted"

    ADD_ROLE          = "addRole"
    ADD_ROLE_RESULT   = "addRoleResult"

    SHOW_DIALOG       =  "showDialog"
    app = None

    def __init__(self):
        self.initializeFacade()

    @staticmethod
    def getInstance():
        return AppFacade()

    def initializeFacade(self):
        super(AppFacade, self).initializeFacade()
        self.initializeController()

    def initializeController(self):
        super(AppFacade, self).initializeController()

        super(AppFacade,self).registerCommand(msg.APP_STARTUP, StartupCommand)
        super(AppFacade,self).registerCommand(msg.SVN_STORE_CONFIG, StoreConfigCmd)
        
        #super(AppFacade,self).registerCommand(msg.APP_END,ExitCmd)
        #super(AppFacade,self).registerCommand(msg.RES_ADD_CATEGORY,CategoryAddCmd)
        
        
    def exitApp(self):
        self.app.ExitMainLoop()
        self.app.Exit()
        

if __name__ == '__main__':
    
    
    app = AppFacade.getInstance()
    app.sendNotification(msg.APP_STARTUP)





