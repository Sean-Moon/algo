import math

def solution(progresses, speeds):
    answer = []
    days_left = []
    
    for i, j in zip(progresses, speeds):
        days_left.append(math.ceil((100 - i)/j))
        
    count = 1
    days_left.reverse()

    print(days_left)      

    while(len(days_left) > 0): 
        print("len days: ", len(days_left))
        top = days_left.pop()
        print(top)
        if(len(days_left)==0):
            print("boom")
            answer.append(1)
            break
        print(days_left[-1])
        while(top >= days_left[-1]):
            days_left.pop()
            count+=1
            if(len(days_left)==0):
                break
        answer.append(count)
        count = 1

    print(answer)
    return answer

pro = [95, 90, 99, 99, 80, 99]
spe = [1, 1, 1, 1, 1, 1]
solution(pro, spe)