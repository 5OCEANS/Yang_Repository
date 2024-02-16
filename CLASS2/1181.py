n=int(input())

word=[]
for i in range(n):
    word.append(input())

set_word = list(set(word))

sort_word=[]
for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word) #리스트를 길이를 기준으로 오름차순으로 정렬하여 result에 할당

for len_word, word in result: #result에 있는 리스트 첫번째 요소를 len_word변수에, 두번째 요소를 word변수에 할당한다. 
    print(word)