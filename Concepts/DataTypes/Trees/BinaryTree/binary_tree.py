from binary_tree_utils import Node



def main():

    rootNode = Node('R')
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')

    rootNode.left = nodeA
    rootNode.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

if __name__ == "__main__":
    main()