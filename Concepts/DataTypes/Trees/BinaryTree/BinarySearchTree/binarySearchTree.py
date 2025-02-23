class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def preOrderTraversal(self):
        if not self.data:
            return
        print(self.data, end=", ")
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    def inOrderTraversal(self):
        if not self.data:
            return
        if self.left:
            self.left.inOrderTraversal()
        print(self.data, end=", ")
        if self.right:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        if not self.data:
            return
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.data, end=", ")

    def search(self, searchValue):
        if self.data == searchValue:
            print(f"{searchValue} exists in binarySearchTree")
            return
        if searchValue < self.data:
            if not self.left:
                print(f"{searchValue} is not exists in binarySearchTree")
                return
            self.left.search(searchValue)
        else:
            if not self.right:
                print(f"{searchValue} is not exists in binarySearchTree")
                return
            self.right.search(searchValue)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data

    def findMax(self):
        if self.right:
            return self.right.findMax()
        return self.data

    def findSum(self):
        total_sum = 0
        if self.data:
            total_sum += self.data
        if self.left:
            total_sum += self.left.findSum()
        if self.right:
            total_sum += self.right.findSum()
        return total_sum

    def delete(self, data):
        if data == self.data:
            if not (self.left or self.right):
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            maxOfLeft = self.left.findMax()
            self.data = maxOfLeft
            return self.left.delete(maxOfLeft)
        elif data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        else:
            if self.right:
                self.right = self.right.delete(data)


if __name__ == "__main__":
    # elements = [13, 7, 15, 8, 19, 14, 3, 18]
    elements = [13, 6, 8, 7, 15, 19, 14, 3, 4, 18]
    binarySearchTree = BinarySearchTree(elements[0])
    for val in elements[1:]:
        binarySearchTree.add_child(val)

    # binarySearchTree.preOrderTraversal()
    # print()

    binarySearchTree.inOrderTraversal()
    print()

    # binarySearchTree.postOrderTraversal()
    # print()

    binarySearchTree.search(5)  # not exists
    binarySearchTree.search(19)  # exists
    binarySearchTree.search(15)  # exists

    print(binarySearchTree.findMin())  # 3
    print(binarySearchTree.findMax())  # 19

    print(binarySearchTree.findSum())

    binarySearchTree.delete(13)

    binarySearchTree.inOrderTraversal()
