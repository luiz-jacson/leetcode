class MyQueue:
    def __init__(self):
        self.queue = list()
        self.inicio = 0
        self.capacidade = len(self.queue)

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return 'null'
        else:
            prim = self.queue[self.inicio]
            self.inicio += 1
            return prim

    def peek(self) -> int:
        return self.queue[self.inicio]

    def empty(self) -> bool:
        return (len(self.queue) == 0 or self.inicio == len(self.queue))


obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())

