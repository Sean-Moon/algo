from collections import deque


def solution(jobs):
    jobs.sort()
    jobs=deque(jobs)
    answer = 0
    taken_times = []

    while(jobs):
        comp_list = []
        top = jobs.popleft()
        print("top ", top)
        taken_times.append(top[1])

        while(jobs): 
            if(jobs[0][0] < top[1]):
                job = jobs.popleft()
                comp_list.append(job)
            else: 
                break
            
        comp_list.sort(key=lambda x: top[1] + x[1])
        print("comp_list", comp_list)

        if(comp_list):
            taken_time = 0
            for i in comp_list:
                taken_times.append(((top[0]+top[1])-i[0])+i[1] + taken_time)
                taken_time = taken_time + i[1]  

    print("taken_times ", taken_times)
    return int(sum(taken_times)/len(taken_times))

jobs = [[3, 23], [22, 4], [23, 2], [30,5], [36,1]]
print(solution(jobs))
