from app.src.metrics import *
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to input file")
args = parser.parse_args()
print("------------------- LOC --------------")

myLoc = loc.LinesOfCode(args.file)
myLoc.countLines()
comments=False
empty=False
imports=False
result = myLoc.getCount(comments, empty, imports)
print(result)

print("------------------- LCOM --------------")

func = lcom4.LCOM4(args.file)
result = func.calculateModuleLCOM4()

print(result)

print("------------------- CBO --------------")
cboFunc = cbo.CBO(args.file)
result = cboFunc.calculateAllCBO()
print(result)

print("------------------- DIT --------------")
obj = False
myDit = dit.DIT(args.file)
result = myDit.calculateAll(obj)
print(result)

print("------------------- NOC --------------")
myNoc = noc.NOC(args.file)
result = myNoc.calculateAll()
print(result)

print("------------------- WMC --------------")
constructor = False
myWmc = wmc.WMC(args.file)
result = myWmc.calculateAll(constructor)

print(result)