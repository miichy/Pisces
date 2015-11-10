#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:Tool.py
# Author:Miichy.Liu
# Created:2015.11.10
# Version:0.1
# Last Modified

# Description: Tool class

from MyLogger import  MyLogger
import sys,argparse

class Tool:
    def __init__(self):
        self.logger = MyLogger().getLogger();
        self.logger.info('Tool class initial ')
        self.exist = True
        self.args = self.arg_parse()

    def arg_parse(self):
        """

        :rtype: object
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--host',dest='hostname')
        parser.add_argument('-u','--user',dest='user')
        parser.add_argument('-c','--command',dest='command')
        parser.add_argument('-k','--key',dest='key')
        return parser.parse_args()


    def jdk_exist(self):
        if self.exist:
            print('jdk exits')
        else:
            print('jdk not exits ')