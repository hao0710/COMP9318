## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    a = x
    y = (a + 1) // 2
    while y < a:
        a = y
        y = (a+ x // a) // 2
    return a
    pass # **replace** this line with your code


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x = x_0
    for i in range(MAX_ITER):
        x_1 = x
        x = x - f(x)/fprime(x)
        if abs(x_1 - x) < EPSILON:
            return x
    return x

################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    tree = Tree(tokens[0])
    child = tree
    parent = Tree(tokens[0])
    root = []
    for i in range(1, len(tokens)):
        if tokens[i] == '[':
            root.append(parent)
            parent = child
            i += 1
        elif tokens[i] == ']':
            i += 1
            parent = root.pop()
            continue
        else:
            child = Tree(tokens[i])
            parent.add_child(child)
    return tree
    pass # **replace** this line with your code    

def max_depth(root): # do not change the heading of the function
    depth = []
    if root.children:
        for child in root.children:
            depth.append(max_depth(child))
        return max(depth) + 1
    else:
        return 1
    pass # **replace** this line with your code





