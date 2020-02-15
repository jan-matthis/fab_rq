import os

import ipdb as pdb
from invoke import task
from redis import Redis

try:
    REDIS_HOST = os.environ["REDIS_HOST"]
except:
    print("Environment variables should contain REDIS_HOST")
try:
    REDIS_PORT = os.environ["REDIS_PORT"]
except:
    print("Environment variables should contain REDIS_PORT")
try:
    REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
except:
    print("Environment variables should contain REDIS_PASSWORD")
try:
    REDIS_DB = os.environ["REDIS_DB"]
except:
    print("Environment variables should contain REDIS_DB")
try:
    REDIS_URL = os.environ["REDIS_URL"]
except:
    print("Environment variables should contain REDIS_URL")


@task
def flush_database(c, all=False):
    """Empties database completely"""

    rc = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB)

    keys = [key.decode() for key in rc.keys()]

    for key in keys:
        rc.delete(key)
        print(f"deleted {key}")


@task
def info(c, section=None):
    """Get redis database info"""
    rc = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB)

    if section is None:
        info = rc.info()
    else:
        info = rc.info(section)

    for key, value in info.items():
        print(f"{key}: {value}")


@task
def interactive(c):
    """Start debugger after establishing redis connection"""

    rc = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB)

    print("Access redis via rc")
    pdb.set_trace()
