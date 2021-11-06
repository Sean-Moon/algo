#-*- coding: utf-8 -*-
#오늘의 업무
related_jobs = [] 
job_count, relation_count = input().split()
jobs = []

for i in range(int(relation_count)):
    related_jobs.append(input())

print(job_count, relation_count)

for i in range(0, int(job_count)):
    jobs.append({'key':chr(65 + i), 'priored': False}) #alphabet

for i in related_jobs:
    candidate = i[0]
    target = i[1]

    swap_candidate = list(filter(lambda x: x['key'] == candidate or x['key'] == target, jobs))
    if(swap_candidate[0]['key'] < candidate and swap_candidate[1]['key'] > target):
        for j in range(len(jobs)):
            if(jobs[j]['key'] == candidate):
#                print("swap candidate ", jobs[j], swap_candidate[0])
                jobs[j] = swap_candidate[0]
            elif(jobs[j]['key'] == target):
 #               print("swap target ", jobs[j], swap_candidate[1])
                jobs[j] = swap_candidate[1]
 
    swap_candidate[0]['priored'] = True
    swap_candidate[1]['priored'] = True

for i in filter(lambda x: x['priored'] == False, jobs):
    for j in range(len(jobs)):
        if(jobs[j]['key'] > i['key']):
            for k in range(len(jobs)):
                if(jobs[k]['key'] == i['key']):
                    jobs[j], jobs[k] = i, jobs[j]
                    break
            break

output = []
for i in jobs:
    output.append(i['key'])

print(''.join(output))


