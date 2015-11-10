#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:AutoD.py
# Author:Miichy.Liu
# Created:2015.11.10
# Version:0.1
# Last Modified

# Description:ssh login in

import pexpect
import subprocess
import sys, getopt
from MyLogger import MyLogger
from Tool import Tool

text = '''
you need to pass two arguments followed by the script name
--host required
--command required/optional
--user required
--key optional
'''


class AutoD:
    def __init__(self, host, comms, key, user, ):
        self.logger = MyLogger().getLogger();
        self.logger.info('AutoD initial beginning~~~')
        self.tool = Tool()

        self.host = host
        self.comms = comms
        if not key:
            # self.child = pexpect.spawn('ssh {0}@{1}'.format(user, host))
            print('ssh commandssss')
            print(host, comms, key, user)
        else:
            # self.child = pexpect.spawn('ssh -i {0} {1}@{2}'.format(key, user, host))
            print('ssh commands')

    def destroyed(self):
        self.logger.info('Destoryed the ssh login ~~~ ')
        subprocess.call(['kill', str(self.child.pid)])

    def exec_command(self):
        self.logger.info('AutoD.exec_command ')
        self.tool.jdk_exist()
        print('command is {}'.format(self.comms))


if (len(sys.argv) < 5):
    print(text)
    sys.exit(1)
else:
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u', ['host=', 'key=','command=' ,'user=','help='])
        print('~~~~~ {0},{1}'.format(opts,args))
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    host = ""
    commands = ""
    key = ""
    user = ""
    for op, value in opts:
        if op == '--host':
            host = value
            print('host value is {}'.format(value))
        elif op == '--command':
            commands = value
            print('commands value is {}'.format(value))
        elif op == '--key':
            key = value
            print('key value is {}'.format(value))
        elif op == '--user':
            user = value
            print('user value is {}'.format(value))
        elif op == '--help':
            print(text)
            sys.exit(1)

autoD = AutoD(host, commands, key, user)
autoD.exec_command()
# autoD.destroyed()
