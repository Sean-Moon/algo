
def getEstimatedTime(stacks):
    estimated_times = []
    for stack in stacks:
        estimated_times.append(stack[0][0] + stack[0][1])
    print("estimated_times: ", estimated_times)
    return int(min(estimated_times))

def getEmptyStack(stacks):
    for stack in stacks:
        if(len(stack) == 0):
            return stack
    return False

def setLines(time, stacks):
    print("setLines")
    tmp_stack = []
    for stack in stacks: 
        if(stack[0][0]+stack[0][1] <= time):
            tmp = stack.pop()
            tmp_stack = stack
            print("pop", tmp)
    return tmp_stack 

def solution(N, sim_data): 
    print(sim_data)

    waitings = []
    stacks = []
    for i in range(N):
        stacks.append([])
    print("--------------")
    print(stacks)

    time = 0

    print("--------------")
    for data in sim_data:
        target = getEmptyStack(stacks)
        print("target", target, "time", time, "data", data)
        # 대기열 존재
        if(target == False): 
            time = getEstimatedTime(stacks)
            print("time", time)
            target = setLines(time, stacks)
            target.append(data)
            if(time - data[0] > 0):
                if(len(waitings) > 0):
                    waitings.append(waitings[-1] + time - data[0])
                else:
                    waitings.append(time - data[0])
                print(waitings)
        # 대기 없으면 바로 작업 할당
        else:
            if(time < data[0]):
                time = data[0]
            target.append(data) 
    print("--------------")
    return sum(waitings)

#   while(heap):
#       duration, start = heappop(heap)
#        time += duration

print(solution(2, [[0,3],[2,5], [4,2],[5,3]]))
print(solution(1, [[2,3],[5,4], [6,3],[7,4]]))
print(solution(2, [[2,3],[5,4], [6,3],[7,4],[8,5],[9,3]]))