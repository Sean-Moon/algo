def factorial_for(m_factorial):
    strs = m_factorial.split('!')

    target_num = int(strs[0])
    factorial_num = len(strs) - 1

    print(target_num, factorial_num)
    i = 0
    answer = 1
    while(True):
        answer = answer*(target_num-factorial_num*i)
        print(answer, i)
        if(factorial_num*i < target_num):
            i+=1
        if(factorial_num*i >= target_num):
            return answer
print(factorial_for("20!!!"))