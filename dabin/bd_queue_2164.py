class CircularQueue:
    
    def __init__(self, size):
        self.size = size + 1
        self.queue = [0] * self.size
        self.front = 0
        self.rear = 0
        self.cur_size = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) %  self.size
    
    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            self.cur_size += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            self.cur_size -= 1
            return self.queue[self.front]
        
    def currentSize(self):
        return self.cur_size
    
    def __len__(self):
        return self.cur_size
    
N = int(input())
queue = CircularQueue(N)
for i in range(1, N+1):
    queue.enqueue(i)

while len(queue) > 1:
    queue.dequeue()
    queue.enqueue(queue.dequeue())

print(queue.dequeue())