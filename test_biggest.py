#-*- coding: utf-8 -*-
import itertools

def checkdigi

def preprocess(numbers): 
    nums_10 = []
    map(lambda x:str(x),numbers)


    return nums

def solution(numbers):
    candidates = []
 
    # n=4, r=2
    result = list(itertools.permutations(numbers,len(numbers)))
    print("**경우의 수 : %s개" % len(result))

    for i in result:
        i = map(lambda x:str(x),i)
        string = ''.join(i)
        candidates.append(string)

    candidates.sort(reverse=True)
    answer = str(candidates[0])
    return answer



input = [1, 10, 100, 1000]

print(solution(input))

#==========================
 
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer