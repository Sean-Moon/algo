a = [1]
b = [1,2]

print(a[-1]) 
print(b[-1]) 

import collections

c = ["marina", "josipa", "nikola", "vinko", "filipa"]
d = ["josipa", "filipa", "marina", "nikola"]

answer = collections.Counter(c) - collections.Counter(d)
print(collections.Counter(c))
print(collections.Counter(d))
print(answer)


