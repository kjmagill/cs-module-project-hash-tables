from dll import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        done = False
        current = self

        while done == False:

            if value < current.value:
                if current.left is None:
                    bst = BSTNode(value)
                    current.left = bst
                    done = True
                else:
                    current = current.left
            else:
                if current.right is None:
                    bst = BSTNode(value)
                    current.right = bst
                    done = True
                else:
                    current = current.right

    def contains(self, target):
        done = False
        current = self

        while done == False:

            if current.value == target:
                return True
            elif current.left is None and current.right is None:
                return False
            elif target < current.value:
                current = current.left
            else:
                current = current.right

    def get_max(self):
        done = False
        current = self

        while done == False:

            if current.right is None:
                return current.value
            else:
                current = current.right

    def for_each(self, fn):
        current = self
        fn(current.value)

        if current.right:
            current.right.for_each(fn)

        if current.left:
            current.left.for_each(fn)

    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(self.value)

        if node.right:
            node.right.in_order_print(node.right)

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.__len__() > 0:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)

            if current_node.right:
                queue.enqueue(current_node.right)

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.__len__() > 0:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left:
                stack.push(current_node.left)

            if current_node.right:
                stack.push(current_node.right)
