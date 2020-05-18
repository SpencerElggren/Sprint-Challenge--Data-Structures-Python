# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None] * capacity
#         self.tail = -1
#         self.head = 0
#         self.index = 0
#         self.length = 0
#
#     def append(self, item):
#         if self.length == self.capacity:
#             self.queue.pop(0)
#             self.queue.append(item)
#         else:
#             self.queue.append(item)
#             self.length += 1
#     def get(self):
#         return self.queue


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [] * capacity

    def append(self, x):
        if len(self.data) == self.capacity:
            self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data
