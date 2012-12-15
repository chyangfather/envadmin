# -*- coding: utf-8 -*-
import wx, msg
from common.filepath import curentDir
from gui.mediator import UpdateDlgMediator, PackageDlgMediator

CFG_SVN_SECTION = 'sVnInFo'
CFG_SVN_ITEMS = ['xmlpath', 'docpath', 'warpath', 'docpath']

CFG_SERVER_SECTION_HEAD = 'sErVerDeF_'
CFG_SERVER_ITEMS = []

TOOLS = {
    1: (u"更新", curentDir() + '/gui/icon/updateIcon.png', "U", 'Update', UpdateDlgMediator),
    2: (u"打包", curentDir() + '/gui/icon/packageIcon.png', 'P', 'Package', PackageDlgMediator),
    }

CTX_MENU_RES_ROOT = {
    101: (u'新建类型', msg.RES_ADD_CATEGORY),
    }

CTX_MENU_RES_CATEGORY = {
    201: (u'新建子类型', msg.RES_ADD_CATEGORY),
    202: (u'新建资源', msg.RES_ADD_RESOURCE),
    }

CTX_MENU_RES_RESOURCE = {
    301: (u'打开', msg.RES_OPEN_RESOURCE),
    302: (u'删除', msg.RES_DEL_RESOURCE),
    }

PROPS_CATEGORY = {
    u'名称': ('name', wx.grid.GridCellTextEditor),
    #''
}

DEPT_NONE_SELECTED = '--None Selected--'
DEPT_ACCT = 'Accounting'
DEPT_SALES = 'Sales'
DEPT_PLANT = 'Plant'
DEPT_SHIPPING = 'Shipping'
DEPT_QC = 'Quality Control'

DeptList = [DEPT_NONE_SELECTED,
            DEPT_ACCT,
            DEPT_SALES,
            DEPT_PLANT
]

ROLE_NONE_SELECTED = '--None Selected--'
ROLE_ADMIN = 'Administrator'
ROLE_ACCT_PAY = 'Accounts Payable'
ROLE_ACCT_RCV = 'Accounts Receivable'
ROLE_EMP_BENEFITS = 'Employee Benefits'
ROLE_GEN_LEDGER = 'General Ledger'
ROLE_PAYROLL = 'Payroll'
ROLE_INVENTORY = 'Inventory'
ROLE_PRODUCTION = 'Production'
ROLE_QUALITY_CTL = 'Quality Control'
ROLE_SALES = 'Sales'
ROLE_ORDERS = 'Orders'
ROLE_CUSTOMERS = 'Customers'
ROLE_SHIPPING = 'Shipping'
ROLE_RETURNS = 'Returns'

RoleList = [ROLE_NONE_SELECTED,
            ROLE_ADMIN,
            ROLE_ACCT_PAY,
            ROLE_ACCT_RCV,
            ROLE_EMP_BENEFITS,
            ROLE_GEN_LEDGER,
            ROLE_PAYROLL,
            ROLE_INVENTORY,
            ROLE_PRODUCTION,
            ROLE_QUALITY_CTL,
            ROLE_SALES,
            ROLE_ORDERS,
            ROLE_CUSTOMERS,
            ROLE_SHIPPING,
            ROLE_RETURNS
]

MAIN_MENU = [#(menuName, [items]     file = wx.Menu; self.menubar.Append(file, menuName)
    (u'File', [
        (101, u"新建资源", "R", wx.ITEM_NORMAL),
        #(id, label, shotKey, style)    file.AppemdItem(wx.MenuTiem(file,id,label,shotKey,style))
        (102, u"新建资源类型", "C", wx.ITEM_NORMAL),
        (103, u"新建视图", "", wx.ITEM_NORMAL),
        (199, u"退出", "", wx.ITEM_NORMAL),
        ])

]
