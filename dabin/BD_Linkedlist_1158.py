class CircularQueue:
    def __init__(self, size):
        self.size = size + 1
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0

    def is_Empty(self):
        return self.front == self.rear

    def is_Full(self):
        return self.front == (self.rear + 1) % self.size
    
    def enqueue(self, data):
        if self.is_Full():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        return True

    def dequeue(self):
        if self.is_Empty():
            return None
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]
        
N, K = map(int, input().split())

cq = CircularQueue(N)
josephus = []

for i in range(1, N+1):
    cq.enqueue(i)

while not cq.is_Empty():
    for _ in range(K - 1):
        data = cq.dequeue()
        if data is not None:
            cq.enqueue(data)
    josephus.append(str(cq.dequeue()))


print("<" + ", " .join(josephus) + ">")