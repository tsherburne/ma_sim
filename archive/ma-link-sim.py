#!/usr/bin/python3

import simpy
import random
import logging
import logging.handlers
import sys
from simmbse import Link, Function

# Setup Logger
logger = logging.getLogger("SimPy")
logger.setLevel(logging.DEBUG)
ls = logging.StreamHandler(sys.stdout)
ls.setLevel(logging.INFO)
logFormat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
ls.setFormatter(logFormat)
logger.addHandler(ls)

SIM_DURATION = 100

def sender(env, link):
    """A process which randomly generates messages."""
    while True:
        # wait for next transmission
        yield env.timeout(5)
        link.put(('Sender sent this at %f' % env.now), 15.0)


def receiver(env, link):
    """A process which consumes messages."""
    while True:
        # Get event for message pipe
        msg = yield link.get()
        print('Received this at %f while %s' % (env.now, msg))


# Setup and start the simulation
print('Event Latency')
env = simpy.Environment()

link = Link(env, capacity=8, delay=5.0)
function = Function(env, "myFunc", logger=logger)
env.process(function.execute())

env.process(sender(env, link))
env.process(receiver(env, link))

env.run(until=SIM_DURATION)