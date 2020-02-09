import ast
from .astUtils import InheritanceTreeBuilder, ClassNodeLister
from ..lib.graph import Graph

class DIT:
    """
        Constructor class that gets in parameter the test file and parse it with "ast"  
    """
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
        self.classNames = []
    """
       method that go through and visit all classes and find classes on the hierarchy of the tree (depth) 
    """
    def findClasses(self):
        classVisiter = ClassNodeLister()
        classVisiter.visit(self.tree)

        classNodes = classVisiter.getClassNodes()
        for node in classNodes:
            self.classNames.append(node.name)
    """"
        method that calls a buildtree and calculate the class's depth and build a tree for each class.
    """
    def calculateAll(self, countObject = False):
        results = {}
        self.findClasses()
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if className in self.classNames:
                results[className] = self.calculateOne(className, countObject)
        return results
    """
        buildTree method is called for building trees
    """
    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(True)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()
    """
        This method calculates one specific class from the current node
    """
    def calculateOne(self, className, countObject = False):
        currentNode = className
        depth = 0
        while len(self.inheritanceTree.graph[currentNode])>0:
            parent = self.inheritanceTree.graph[currentNode][0]
            if parent == "object":
                if countObject:
                    depth += 1
            elif not parent == "~":
                depth += 1
            currentNode = parent

        return depth




    