#!/usr/bin/python3

import argparse
import simpy
import logging
import logging.handlers
import sys
import json
from simmbse import Branch
from utility import build_index

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="System Model Input File")
parser.add_argument("main_function", help="Function to Simulate.")
args = parser.parse_args()

# Load System Model
with open(args.input_file, 'r') as inf:
    systemModel = json.load(inf)
    inf.close()

# Setup Logger
logger = logging.getLogger("SimMA")
logger.setLevel(logging.DEBUG)
ls = logging.StreamHandler(sys.stdout)
ls.setLevel(logging.INFO)
logFormat = logging.Formatter(
    '%(asctime)s : %(name)s : %(levelname)s : %(message)s')
ls.setFormatter(logFormat)
logger.addHandler(ls)

# Initialize SimPy
env = simpy.Environment()

# Main function
def main():
    # Build System Model Index
    build_index(systemModel)

    mainStructure = None
    for call in systemModel['data']['cpsSystemModel']['callStructure']:
        if call['function']['name'] == args.main_function:
            print("Parsing %s Branch...." % (args.main_function))
            mainStructure = Branch(
                env, logger, "0", systemModel, call['structure'])
            break

    if mainStructure is not None:
        print(mainStructure)

        print("Simulate %s Branch...." % (args.main_function))
        env.process(mainStructure.simulate())
        env.run(until=200)
    else:
        print("Function: %s not found!" % (args.main_function))


if __name__ == "__main__":
    main()
