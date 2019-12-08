import logging
import os

def getLogger(prefixName):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger