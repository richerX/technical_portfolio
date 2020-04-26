class Stack():
    def __init__(self):
        self.data = []
        self.length = 0

    def empty(self):
        return self.length == 0
    
    def push(self, value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.data.pop()

    def back(self):
        return self.data[-1]

    def size(self):
        return self.length

    def clear(self):
        self.__init__()
        
    def get(self):
        return self.data


class Queue():
    def __init__(self):
        self.data = []
        self.head = 0
        self.length = 0
    
    def push(self, value):
        self.data.append(value)
        self.length += 1          

    def pop(self):
        result = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        self.length -= 1
        return result

    def front(self):
        return self.data[self.head]
    
    def size(self):
        return self.length
        
    def empty(self):
        return self.length == 0
    
    def clear(self):
        self.__init__()  
        
    def get(self):
        return self.data


class Deque():
    def __init__(self):
        self.data_front = []
        self.data_back = []
        self.front = -1
        self.back = -1
        self.length = 0
        
    def push_front(self, value):
        if self.front >= -1:
            self.data_front.append(value)
        else:
            self.data_back[abs(self.front + 2)] = value
        self.front += 1 
        self.length += 1
    
    def push_back(self, value):
        if self.back >= -1:
            self.data_back.append(value)
        else:
            self.data_front[abs(self.back + 2)] = value
        self.back += 1 
        self.length += 1

    def pop_front(self):
        if self.front >= 0:
            result = self.data_front.pop()
        else:
            result = self.data_back[abs(self.front + 1)]
            self.data_back[abs(self.front + 1)] = None
        self.front -= 1
        self.length -= 1
        return result

    def pop_back(self):
        if self.back >= 0:
            result = self.data_back.pop()
        else:
            result = self.data_front[abs(self.back + 1)]
            self.data_front[abs(self.back + 1)] = None
        self.back -= 1
        self.length -= 1
        return result
    
    def get_front(self):
        if self.front >= 0:
            return self.data_front[self.front]
        return self.data_back[abs(self.front + 1)]
    
    def get_back(self):
        if self.back >= 0:
            return self.data_back[self.back]
        return self.data_front[abs(self.back + 1)]
    
    def size(self):
        return self.length
        
    def empty(self):
        return self.length == 0
    
    def clear(self):
        self.__init__()    
        
    def get(self):
        return list(reversed(self.data_back)) + self.data_front


class LinkedListNode:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.prev.value} <-> {self.value} <-> {self.next.value}"


class LinkedList:
    def __init__(self):
        self.data = []
        self.length = 0
    
    def __str__(self):
        result = ""
        for node in self.data:
            result += str(node.value) + " <-> "
        return result[:-5]
    
    def append(self, value):
        new_node = LinkedListNode(value, None, None)
        self.data.append(new_node)
        if self.length >= 1:
            self.data[-2].next = self.data[-1]
            self.data[-1].prev = self.data[-2]
        self.length += 1
    
    def empty(self):
        return self.length == 0
    
    def clear(self):
        self.__init__()
    
    def get(self):
        return self.data
