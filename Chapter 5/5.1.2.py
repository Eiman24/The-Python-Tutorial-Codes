from collections import deque
# deque was designed to have fast appends and pops from both ends
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()

queue.popleft()

print(queue)

#attention Eiman is cutting in line
queue.appendleft('Eiman')
print(queue)