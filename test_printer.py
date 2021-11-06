from collections import deque

class Task:
    def __init__(self, task_id, task_priority):
        self.id = task_id
        self.priority = task_priority
    def __repr__(self):
        return "<Task id:%s priority:%s>" % (self.id, self.priority)
    def __str__(self):
        return "id is %s, priority is %s" % (self.id, self.priority)

def solution(priorities, location):
    answer = 0
    queue = []
    for i in range(0, len(priorities)):
        queue.append(Task(i, priorities[i]))

#    print(queue)
    queue = deque(queue) 
    priored_list = []

    while(len(queue) > 0):
        task = queue.popleft()
        result = isPrior(queue, task)
        if(result == True): 
            priored_list.append(task)
        else: 
            queue.append(task)
        
    print(priored_list)
    for i in range(0, len(priored_list)):
        if(priored_list[i].id == location):
            return i + 1 

def isPrior(queue, j):
    if(len(queue) == 0): 
        return True

    for i in range(0, len(queue)) :
        if(j.priority < queue[i].priority):
            return False
    return True

sec = [1, 1, 9, 1, 1, 1]

print(solution(sec, 0))



#########################################

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer