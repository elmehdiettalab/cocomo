import ast
from .astUtils import ClassNodeLister, FunctionNodeLister


"""
    class that weights the sum of complexity of all methods in the class.
"""
class WMC:
    """
        Constructor class that gets the file and store it then parse it.
    """
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
    """
        method that invokes on each class the method calculateOne that computes the sum of complexity
    """
    def calculateAll(self, countInit = False):
        results = {}
        classLister = ClassNodeLister()
        classLister.visit(self.tree)
        classes = classLister.getClassNodes()
        for classNode in classes:
            results[classNode.name] = self.calculateOne(classNode, countInit)
        return results

    def calculateOne(self, classNode, countInit = False):
        methodCount = 0
        functionLister = FunctionNodeLister()
        functionLister.visit(classNode)
        functions = functionLister.getFunctionNodes()

        for func in functions:
            if func.name == "__init__":
                if countInit:
                    methodCount += 1
            else:
                methodCount += 1
        return methodCount




    