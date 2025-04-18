from logger import logging

def add(a,b):
    logging.debug("this is a addition operation taking place")
    return a+b

logging.debug("addition operation happend")

add(12,5)