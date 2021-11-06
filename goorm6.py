#-*- coding: utf-8 -*-
#대소문자 바꾸어 출력
characters = list(input())
changed_characters = []
characters.reverse()
while(characters):
    top = characters.pop()
    ascii_code = ord(top)
    if(ascii_code >= 65 and ascii_code <= 90): # Upper Case
        changed_characters.append(top.lower())
    elif(ascii_code >= 97 and ascii_code <= 122): # Lower Case
        changed_characters.append(top.upper())
    else:
        changed_characters.append(top)

print(''.join(changed_characters))