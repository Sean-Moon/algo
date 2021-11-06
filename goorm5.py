#-*- coding: utf-8 -*-
#알파벳 빈도
from collections import Counter 

texts = input().split()
lower_caracters = []
while(texts):
    lower_caracters += list(texts.pop().lower())

counter = Counter(lower_caracters)
print("a : %s" % counter['a'])
print("b : %s" % counter['b'])
print("c : %s" % counter['c'])
print("d : %s" % counter['d'])
print("e : %s" % counter['e'])
print("f : %s" % counter['f'])
print("g : %s" % counter['g'])
print("h : %s" % counter['h'])
print("i : %s" % counter['i'])
print("j : %s" % counter['j'])
print("k : %s" % counter['k'])
print("l : %s" % counter['l'])
print("m : %s" % counter['m'])
print("n : %s" % counter['n'])
print("o : %s" % counter['o'])
print("p : %s" % counter['p'])
print("q : %s" % counter['q'])
print("r : %s" % counter['r'])
print("s : %s" % counter['s'])
print("t : %s" % counter['t'])
print("u : %s" % counter['u'])
print("v : %s" % counter['v'])
print("w : %s" % counter['w'])
print("x : %s" % counter['x'])
print("y : %s" % counter['y'])
print("z : %s" % counter['z'])
#print(pd.Series(lower_caracters).value_counts())