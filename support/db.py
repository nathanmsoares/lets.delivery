import logging
import random
import os
import redis
import socket


__all__ = ["logger", "init_db", "connect_db", "db"]


def initLog():
    log = logging.getLogger()    # root logger
    log.setLevel(logging.DEBUG)
    
    # log to console 
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # create formatter
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    
    log.addHandler(ch)
    return log

logger = initLog()

random.seed(os.urandom(128))

db: redis.StrictRedis = None

def connect_db():    
    database = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    cname = "webingo_{}_{}".format(socket.gethostname(), os.getpid())
    database.client_setname(cname)
    
    logger.info('connected to persistency db as {}'.format(cname))
    return database

def init_db():
    global db
    db = connect_db()

def get_db():
    global db
    return db
