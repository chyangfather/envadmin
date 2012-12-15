#!/usr/bin/python
#-*-coding:utf-8-*-
#配置文件
__author__ = 'holbrook'
CFG_FILE = 'conf/config.conf'
IGNORED_XML = [
    '/.svn/',                       # svn folder
    'studio.xml',                   # livebos project file
    'customFuncFactor.xml',         # 运行配置-自定义功能权限要素

    '/.userproject/',
    'systemmenu.xml',               # 运行配置-服务器对象配置
    '_menu.xml',


    '/portalschemes/',              # wrong folder
    '_layout.xml',                  #workflow layout



    'menu.xml',
    

    'deletedStudio.xml',            #
    'scheme-config.xml',
    ]

COMMIT_BO_URL_HEAD = ''

