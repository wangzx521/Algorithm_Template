class queue:
    def __init__(self):
        self.__items = []
    def enqueue(self, __item):
        self.__items.insert(0, __item)
    def dequeue(self):
        return self.__items.pop()
    def is_empty(self):
        return not bool(self.__items)
    def size(self):
        return len(self.__items)
    

def hot_potato(namelist , num):
    sim_queue = queue()
    for name in namelist:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 1))

a = queue()
print(a._queue__items)
