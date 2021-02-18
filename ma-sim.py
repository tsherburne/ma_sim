#!/usr/bin/python3

import simpy
import random
import logging
import logging.handlers
import sys

# Setup Logger
logger = logging.getLogger("SimPy")
logger.setLevel(logging.DEBUG)
ls = logging.StreamHandler(sys.stdout)
ls.setLevel(logging.INFO)
logFormat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
ls.setFormatter(logFormat)
logger.addHandler(ls)

# Initialize SimPy
env = simpy.Environment()

def f0(env, level):
    print("Start %s at %d" % (level, env.now))
    eb1 = env.process(b1(env, level + ".b1"))
    eb2 = env.process(b2(env, level + ".b2"))
    eb3 = env.process(b3(env, level + ".b3"))
    yield eb1 & eb2 & eb3
    print("Finish %s at %d" % (level, env.now))

def b1(env, level):
    print("Start %s at %d" % (level, env.now))
    e1 = env.process(f1(env, level + ".f1"))
    yield e1
    e2 = env.process(f2(env, level + ".f2"))
    yield e2
    e3 = env.process(f3(env, level + ".f3"))
    yield e1 & e2 & e3
    print("Finish %s at %d" % (level, env.now))

def b2(env, level):
    print("Start %s at %d" % (level, env.now))
    e3 = env.process(f3(env, level + ".f3"))
    yield e3
    e2 = env.process(f2(env, level + ".f2"))
    yield e2
    e1 = env.process(f1(env, level + ".f1"))
    yield e1 & e2 & e3
    print("Finish %s at %d" % (level, env.now))

def b3(env, level):
    print("Start %s at %d" % (level, env.now))
    funcList = ["f1", "f2", "f3"]
    selected = random.choices(funcList, weights = [10, 10, 1], k = 1)
    selectedFunc = globals()[selected[0]]
    print("Selected: " + str(selectedFunc))
    e = env.process(selectedFunc(env, level + "." + selected[0]))
    yield e
    print("Finish %s at %d" % (level, env.now))

def f1(env, level):
    logger.info("Start %s at %d" % (level, env.now))
    yield env.timeout(3)
    logger.info("Finish %s at %d" % (level, env.now))

def f2(env, level):
    logger.info("Start %s at %d" % (level, env.now))
    yield env.timeout(2)
    logger.info("Finish %s at %d" % (level, env.now))

def f3(env, level):
    logger.info("Start %s at %d" % (level, env.now))
    yield env.timeout(1)
    logger.info("Finish %s at %d" % (level, env.now))

env.process(f0(env, "f0"))
env.run(until=10)