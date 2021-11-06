#-*- coding: utf-8 -*-
#이효리 문제
text = input() 

def isPalindrome(text):
    for i in range(int(len(text)/2)):
    	if text[i] != text[(len(text)-1)-i]:
    		return False
    return True

if(isPalindrome(text)): 
    print("Palindrome")
else: 
    print("Not Palindrome")