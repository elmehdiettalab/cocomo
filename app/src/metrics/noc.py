import ast
from .astUtils import InheritanceTreeBuilder,ClassNodeLister

class NOC:
    """
        Constructor method that stores the file path and parse it.
    """
    def __init__(self, filepath):
        self.file = filepath
        f = open(self.file)
        self.tree = ast.parse(f.read())
        f.close()
        self.classNames = []
    """
        this method stores classes in an array "classnames" 
    """
    def findClasses(self):
        classVisiter = ClassNodeLister()
        classVisiter.visit(self.tree)

        classNodes = classVisiter.getClassNodes()
        for node in classNodes:
            self.classNames.append(node.name)
    """
        method that calculates all children of each class and store in results, 
        and it builds a tree for each node(class) 
    """
    def calculateAll(self):
        results = {}
        self.findClasses()
        self.buildTree()
        for className in self.inheritanceTree.graph:
            if className in self.classNames:
                results[className] = self.calculateOne(className)
        return results
    """
        helper method that builds a tree from current node
    """
    def buildTree(self):
        treeBuilder = InheritanceTreeBuilder(False)
        treeBuilder.visit(self.tree)
        self.inheritanceTree = treeBuilder.getTree()

    """
        method that calculates the length of a given class' children.
    """
    def calculateOne(self, className):
        return len(self.inheritanceTree.graph[className])

