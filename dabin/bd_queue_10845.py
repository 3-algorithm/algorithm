class CircularQueue:
    def __init__(self, size):
        self.size = size + 1
        self.queue = [0] * self.size
        self.front = 0
        self.rear = 0
        self.cur_size = 0

    def isEmpty(self):
        return 1 if self.front == self.rear else 0
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.size
    
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
        else:
            return -1
        
    def peek_front(self):
        if not self.isEmpty():
            next_index = (self.front + 1) % self.size
            return self.queue[next_index]
        else:
            return -1
        
    def peek_back(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            return -1
        
    def currentSize(self):
        return self.cur_size

N = int(input())
cq = CircularQueue(N)
result = []

for _ in range(N):
    
    arr = input().split()

    order = arr[0]

    if order == 'push':
        cq.enqueue(arr[1])

    elif order == 'pop':
        result.append(str(cq.dequeue()))

    elif order == 'empty':
        result.append(str(cq.isEmpty()))
    
    elif order == 'front':
        result.append(str(cq.peek_front()))

    elif order == 'back':
        result.append(str(cq.peek_back()))

    elif order == 'size':
        result.append(str(cq.currentSize()))

print('\n'.join(result))