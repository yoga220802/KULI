from collections import deque

class Queue:
    def __init__ (self):
        self.queue = deque([])

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.popleft()
    
    def clear_queue(self):
        self.queue.clear()
    
    def show_queue(self):
        for i in range(len(self.queue)):
            print(f"{i+1}. {self.queue[i]}")