from heapq import *

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    print(h)
    return [heappop(h) for i in range(len(h))]

#print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1,  'write spec'))
heappush(h, (3,  'create tests'))
heappush(h, (3,  'create tests1'))

print(heapsort(h))