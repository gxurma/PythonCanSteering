#!/usr/bin/env python3


import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
for i in range(5):
    q.put(i)
q.put('valami')
q.put(b'valami')

while not q.empty():
    print(type(q.get()))
print()

q = queue.LifoQueue()

for i in range(5):
    q.put(i)
q.put('valami')
q.put(b'valami')

while not q.empty():
    print(q.get(), end=' ')
print()
