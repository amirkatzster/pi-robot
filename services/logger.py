import logging
import sys

def setLogger(moduleName):
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    handler = logging.FileHandler('logs/{}.log'.format(moduleName))
    handler.setLevel(logging.INFO)
    root.addHandler(ch)
    root.addHandler(handler)
