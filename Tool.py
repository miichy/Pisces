#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:Tool.py
# Author:Miichy.Liu
# Created:2015.11.10
# Version:0.1
# Last Modified

# Description: Tool class

from MyLogger import  MyLogger

class Tool:
    def __init__(self):
        self.logger = MyLogger().getLogger();
        self.logger.info('Tool class initial ')
        self.exist = True

    def jdk_exist(self):
        if self.exist:
            print('jdk exits')
        else:
            print('jdk not exits ')