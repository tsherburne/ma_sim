#!/usr/bin/python3

import simpy
import logging
import logging.handlers
import sys
import json
from simmbse import Branch
from utility import build_index

# Load System Model
with open('./function.json', 'r') as inf:
    systemModel = json.load(inf)
    inf.close()

# Setup Logger
logger = logging.getLogger("SimMA")
logger.setLevel(logging.DEBUG)
ls = logging.StreamHandler(sys.stdout)
ls.setLevel(logging.INFO)
logFormat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
ls.setFormatter(logFormat)
logger.addHandler(ls)

# Initialize SimPy
env = simpy.Environment()

# Main function
def main():
    build_index(systemModel)
    mainStructure = None
    for call in systemModel['data']['cpsSystemModel']['callStructure']:
        if call['function']['name'] == "Main":
            print("Parsing Main Branch....")
            mainStructure = Branch(env, logger, "0", systemModel, call['structure'])
            break


    print(mainStructure)

    env.process(mainStructure.simulate())
    env.run(until=200)

if __name__ == "__main__":
    main()
