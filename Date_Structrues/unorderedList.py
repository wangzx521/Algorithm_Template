class Node:
    def __init__(self , node_data = None):
        self.node_data = node_data
        self._next = None
    @property
    def data(self):
        return self.node_data
    @data.setter
    def set_data(self , node_data):
        self.node_data = node_data
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, next_node):
        self._next = next_node
class UnorderedList:
    def __init__(self,head = None):
        self.head = head
    def is_empty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            else:
                current = current.next 
        return False
    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            else:
                previous = current
                current = current.next
                if current == None:
                    raise ValueError(f'(item) is not in the list')
                elif previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        if current is None:
            self.head = temp 
        else:
            while current is not None:
                previous = current
                current = current.next
            previous.next = temp
#通过实现getitem方法实现按下标访问 如：a[0]
    def __getitem__(self, ind):
        if ind >= 0:
            current_num = 0
            current = self.head
            while ind != current_num and current is not None:
                current_num += 1
                current = current.next
            if current_num != ind:
                raise IndexError('out of range index')
            return current.data
        else:
            
    def insert(self, index , item):
        temp = Node(item)
        if index == 0:
            self.head.next = temp
        else:
            current_num = 0
            current = self.head
            previous = None
            while index != current_num and current is not None:
                previous = current
                current = current.next

a = UnorderedList()
a.append(3)
a.append(1)
a.append(2)
print(a[2])
a.insert(2 , 10)
print(a[2], a[3])


