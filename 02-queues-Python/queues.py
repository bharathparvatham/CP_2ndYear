"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        if len(self.storage) == 1 and self.storage[0] == None:
            self.storage[0] = new_element
        else:
            self.storage.insert(0, new_element)

    def peek(self):
        if len(self.storage) == 0:
            return None
        return self.storage[-1]

    def dequeue(self):
        if (len(self.storage) == 1 and self.storage[0] == None) or (len(self.storage) == 0):
            pass
        else:
            self.storage = self.storage[0:len(self.storage) - 1]
