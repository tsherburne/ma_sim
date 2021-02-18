#!/usr/bin/python3

import json

with open('./function.json', 'r') as inf:
    funcStructure = json.load(inf)
    inf.close()

# Output Generated Simuulation Code
outf = open('./gen-sim.py', 'w')
outf.seek(0)
outf.flush()

global depth
depth = 0

global currentFunction
currentFunction = ""

# Header Code
def header():
    head = '''#!/usr/bin/python3

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
'''
    outf.write(head)

# Footer Code
def footer():
    foot = '''
# Start simulation
env.process(Main(env))
env.run(until=25)
'''
    outf.write(foot)
    outf.flush()
    outf.close()

def numberStructure(structure):
    global currentFunction, depth

    # number breadth
    for num, struct in enumerate(structure['structure'], start=1):
        if depth == 0:
            struct['number'] = structure['number'] + str(num)
        else:
            struct['number'] = structure['number'] + "." + str(num)

    # Recurse down next level
    for struct in structure['structure']:
        depth +=1
        numberStructure(struct)
        depth -=1

def printStructure(structure):
    global currentFunction, depth

    if depth == 0:
        print(" " *depth + "%s: 0:%s" % (currentFunction, structure['type']))
    else:
        if structure['type'] == "Function":
            print(" " *depth + "%s: %s:%s:%s" %
                (currentFunction, structure['number'], structure['type'], structure['referenceName']))
        else:
            print(" " *depth + "%s: %s:%s" %
                (currentFunction, structure['number'], structure['type']))

    # print depth first
    for struct in structure['structure']:
        depth +=1
        printStructure(struct)
        depth -=1

def parseStructure(structure):
    global currentFunction
    eventList = []
    fname = currentFunction + structure['number'].replace(".", "_")
    structLen = len(structure['structure'])

    if structure['type'] == "Branch":
        outf.write("def " + fname + "(env):\n")
        outf.write("    logger.info('Branch Start: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")
        # execute in series
        for num, struct in enumerate(structure['structure'], start=1):
            bname = currentFunction + struct['number'].replace(".", "_")
            ename = "b" + str(num)
            outf.write("    " + ename + " = env.process(" + bname + "(env))\n")
            outf.write("    yield " + ename + "\n")

        outf.write("    logger.info('Branch End: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

    elif structure['type'] == "Parallel":
        outf.write("def " + fname + "(env):\n")
        outf.write("    logger.info('Parallel Start: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

        yieldString = "yield "

        # execute in parallel
        for num, struct in enumerate(structure['structure'], start=1):
            bname = currentFunction + struct['number'].replace(".", "_")
            ename = "b" + str(num)
            outf.write("    " + ename + " = env.process(" + bname + "(env))\n")
            eventList.append(ename)
            # wait for all branches to complete
            yieldString += ename
            if num < structLen:
                yieldString += " & "

        outf.write("    " + yieldString +"\n")
        outf.write("    logger.info('Parallel End: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

    elif structure['type'] == "Select":
        outf.write("def " + fname + "(env):\n")
        outf.write("    logger.info('Select Start: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

        # select one of
        funcList = "funcList = ["
        for num, struct in enumerate(structure['structure'], start=1):
            bname = currentFunction + struct['number'].replace(".", "_")
            funcList += "'" + bname + "'"
            if num < structLen:
                funcList += ", "

        funcList += "]"
        outf.write("    " + funcList + "\n")
        outf.write("    selected = random.choices(funcList, k=1)\n")
        outf.write("    selectedFunc = globals()[selected[0]]\n")
        outf.write("    sb = env.process(selectedFunc(env))\n")
        outf.write("    yield sb\n")
        outf.write("    logger.info('Select End: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

    elif structure['type'] == "Loop":
        outf.write("def " + fname + "(env):\n")
        outf.write("    logger.info('Loop Start: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")
        outf.write("    while True:\n")
        loopFunction = currentFunction + structure['structure'][0]['number'].replace(".", "_")
        outf.write("        lb = env.process(" + loopFunction + "(env))\n")
        outf.write("        yield lb\n")
        outf.write("    logger.info('Loop End: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")

    elif structure['type'] == "Function":
        outf.write("def " + fname + "(env):\n")
        outf.write("    logger.info('Function Start: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")
        outf.write("    fb = env.process(" + structure['referenceName'] + "(env))\n")
        outf.write("    yield fb\n")
        outf.write("    logger.info('Function End: " + "%s" %
            (fname) + " at: %d' % (env.now))\n")
    # print depth first
    for struct in structure['structure']:
        parseStructure(struct)

def main():
    global currentFunction, depth

    # Output header
    header()
    # loop through all functions
    for call in funcStructure['data']['cpsSystemModel']['callStructure']:
        currentFunction = call['function']['name']
        print(currentFunction)

        if call['structure']['structure']: # decomposition exits
            # recursively parse call structure for function
            # outf.write("    yield env.process(" + currentFunction + "__(env))\n")
            # outf.write("    logger.info('End: " + "%s" % (currentFunction) + " at: %d' % (env.now))\n")
            call['structure']['number'] = ""
            numberStructure(call['structure'])
            printStructure(call['structure'])
            parseStructure(call['structure'])
        else:
            outf.write("def " + currentFunction + "(env):\n")
            outf.write("    logger.info('Start: " + "%s" % (currentFunction) + " at: %d' % (env.now))\n")
            outf.write("    yield env.timeout(2)\n")
            outf.write("    logger.info('End: " + "%s" % (currentFunction) + " at: %d' % (env.now))\n")
    # output footer
    footer()

if __name__ == "__main__":
    main()