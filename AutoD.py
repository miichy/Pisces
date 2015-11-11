#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:AutoD.py
# Author:Miichy.Liu
# Created:2015.11.10
# Version:0.1
# Last Modified

# Description:ssh login in

#import pexpect
from pexpect import *

from MyLogger import MyLogger
from Tool import Tool

text = '''
you need to pass two arguments followed by the script name
--host required
--command required/optional
--user required
--key optional
'''
error = '''ImportError:No module named termios'''

class AutoD:
    def __init__(self, host, comms, key, user, ):

        self.logger = MyLogger().getLogger();
        self.logger.info('AutoD initial beginning~~~')
        self.tool = Tool()

        self.host = host
        self.comms = comms
        if not key:
            self.child = run('ssh {0}@{1}'.format(user, host))
        else:
            self.child = run('ssh -i {0} {1}@{2}'.format(key, user, host))

    def destroyed(self):
        self.logger.info('Destoryed the ssh login ~~~ ')
        self.child.close(force=True)

    def exec_command(self):
        self.logger.info('AutoD.exec_command ')
        self.tool.jdk_exist()
        print('command is {}'.format(self.comms))


args = Tool().arg_parse();
autoD = AutoD(args.hostname, args.command, args.key, args.user)
autoD.exec_command()
autoD.destroyed()
