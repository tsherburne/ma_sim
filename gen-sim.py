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
def f1(env):
    logger.info('Start: f1 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f1 at: %d' % (env.now))
def f2(env):
    logger.info('Start: f2 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f2 at: %d' % (env.now))
def f3(env):
    logger.info('Start: f3 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f3 at: %d' % (env.now))
def f4(env):
    logger.info('Start: f4 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f4 at: %d' % (env.now))
def f5(env):
    logger.info('Start: f5 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f5 at: %d' % (env.now))
def f6(env):
    logger.info('Start: f6 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f6 at: %d' % (env.now))
def f7(env):
    logger.info('Start: f7 at: %d' % (env.now))
    yield env.timeout(2)
    logger.info('End: f7 at: %d' % (env.now))
def Main(env):
    logger.info('Branch Start: Main at: %d' % (env.now))
    b1 = env.process(Main1(env))
    yield b1
    logger.info('Branch End: Main at: %d' % (env.now))
def Main1(env):
    logger.info('Parallel Start: Main1 at: %d' % (env.now))
    b1 = env.process(Main1_1(env))
    b2 = env.process(Main1_2(env))
    yield b1 & b2
    logger.info('Parallel End: Main1 at: %d' % (env.now))
def Main1_1(env):
    logger.info('Branch Start: Main1_1 at: %d' % (env.now))
    b1 = env.process(Main1_1_1(env))
    yield b1
    b2 = env.process(Main1_1_2(env))
    yield b2
    b3 = env.process(Main1_1_3(env))
    yield b3
    logger.info('Branch End: Main1_1 at: %d' % (env.now))
def Main1_1_1(env):
    logger.info('Function Start: Main1_1_1 at: %d' % (env.now))
    fb = env.process(f1(env))
    yield fb
    logger.info('Function End: Main1_1_1 at: %d' % (env.now))
def Main1_1_2(env):
    logger.info('Function Start: Main1_1_2 at: %d' % (env.now))
    fb = env.process(f3(env))
    yield fb
    logger.info('Function End: Main1_1_2 at: %d' % (env.now))
def Main1_1_3(env):
    logger.info('Parallel Start: Main1_1_3 at: %d' % (env.now))
    b1 = env.process(Main1_1_3_1(env))
    b2 = env.process(Main1_1_3_2(env))
    yield b1 & b2
    logger.info('Parallel End: Main1_1_3 at: %d' % (env.now))
def Main1_1_3_1(env):
    logger.info('Branch Start: Main1_1_3_1 at: %d' % (env.now))
    b1 = env.process(Main1_1_3_1_1(env))
    yield b1
    logger.info('Branch End: Main1_1_3_1 at: %d' % (env.now))
def Main1_1_3_1_1(env):
    logger.info('Select Start: Main1_1_3_1_1 at: %d' % (env.now))
    funcList = ['Main1_1_3_1_1_1', 'Main1_1_3_1_1_2']
    selected = random.choices(funcList, k=1)
    selectedFunc = globals()[selected[0]]
    sb = env.process(selectedFunc(env))
    yield sb
    logger.info('Select End: Main1_1_3_1_1 at: %d' % (env.now))
def Main1_1_3_1_1_1(env):
    logger.info('Branch Start: Main1_1_3_1_1_1 at: %d' % (env.now))
    b1 = env.process(Main1_1_3_1_1_1_1(env))
    yield b1
    logger.info('Branch End: Main1_1_3_1_1_1 at: %d' % (env.now))
def Main1_1_3_1_1_1_1(env):
    logger.info('Function Start: Main1_1_3_1_1_1_1 at: %d' % (env.now))
    fb = env.process(f5(env))
    yield fb
    logger.info('Function End: Main1_1_3_1_1_1_1 at: %d' % (env.now))
def Main1_1_3_1_1_2(env):
    logger.info('Branch Start: Main1_1_3_1_1_2 at: %d' % (env.now))
    b1 = env.process(Main1_1_3_1_1_2_1(env))
    yield b1
    b2 = env.process(Main1_1_3_1_1_2_2(env))
    yield b2
    logger.info('Branch End: Main1_1_3_1_1_2 at: %d' % (env.now))
def Main1_1_3_1_1_2_1(env):
    logger.info('Function Start: Main1_1_3_1_1_2_1 at: %d' % (env.now))
    fb = env.process(f6(env))
    yield fb
    logger.info('Function End: Main1_1_3_1_1_2_1 at: %d' % (env.now))
def Main1_1_3_1_1_2_2(env):
    logger.info('Function Start: Main1_1_3_1_1_2_2 at: %d' % (env.now))
    fb = env.process(f7(env))
    yield fb
    logger.info('Function End: Main1_1_3_1_1_2_2 at: %d' % (env.now))
def Main1_1_3_2(env):
    logger.info('Branch Start: Main1_1_3_2 at: %d' % (env.now))
    b1 = env.process(Main1_1_3_2_1(env))
    yield b1
    logger.info('Branch End: Main1_1_3_2 at: %d' % (env.now))
def Main1_1_3_2_1(env):
    logger.info('Function Start: Main1_1_3_2_1 at: %d' % (env.now))
    fb = env.process(f4(env))
    yield fb
    logger.info('Function End: Main1_1_3_2_1 at: %d' % (env.now))
def Main1_2(env):
    logger.info('Branch Start: Main1_2 at: %d' % (env.now))
    b1 = env.process(Main1_2_1(env))
    yield b1
    logger.info('Branch End: Main1_2 at: %d' % (env.now))
def Main1_2_1(env):
    logger.info('Loop Start: Main1_2_1 at: %d' % (env.now))
    while True:
        lb = env.process(Main1_2_1_1(env))
        yield lb
    logger.info('Loop End: Main1_2_1 at: %d' % (env.now))
def Main1_2_1_1(env):
    logger.info('Branch Start: Main1_2_1_1 at: %d' % (env.now))
    b1 = env.process(Main1_2_1_1_1(env))
    yield b1
    logger.info('Branch End: Main1_2_1_1 at: %d' % (env.now))
def Main1_2_1_1_1(env):
    logger.info('Function Start: Main1_2_1_1_1 at: %d' % (env.now))
    fb = env.process(f2(env))
    yield fb
    logger.info('Function End: Main1_2_1_1_1 at: %d' % (env.now))

# Start simulation
env.process(Main(env))
env.run(until=25)
