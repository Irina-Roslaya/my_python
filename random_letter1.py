import random
list1=['самовар','весна','лето']
length=len(list1)
num=random.randint(1,length)
word=list1[num]
leng=len(word)
numb=random.randint(1,leng)
word = word[:numb-1]+'?'+ word[numb:]
print(word)
n=input('Введите букву:')
word1=word[:numb-1]+ n + word[numb:]
if word1==list1[num]:
    print('Победа!')
    print('Слово:',list1[num])
else:
    print('Увы! Попробуйте в другой раз.')
    print('Слово:',list1[num])
