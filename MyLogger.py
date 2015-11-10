#!/usr/bin/env  python
# -*- coding : utf-8 -*-

# Script Name:MyLogger.py
# Author:Miichy.Liu
# Created:2015.11.10
# Version:0.1
# Last Modified

# Description: Logger class

import logging
from logging.handlers import TimedRotatingFileHandler

class MyLogger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('autoD')
        FORMAT = "%(asctime)-15s  %(message)s"
        logFormatter = logging.Formatter(FORMAT)
        logHandler = TimedRotatingFileHandler('autoD.log',when='midnight')
        logHandler.suffix = '%Y%m%d'
        logHandler.setFormatter(logFormatter)
        self.logger.addHandler(logHandler)

    #def setLogger(self):

    def getLogger(self):
        return self.logger