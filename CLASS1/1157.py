word = input().upper()
word_list = list(set(word)) #중복 제거해서 리스트에 넣기

cnt = [] #각 문자가 쓰여진 횟수를 저장하는 변수 
for i in word_list:
  count = word.count #conut에 word.count함수 할당
  cnt.append(count(i)) #HELLO라면 H가 1번 이니까 cnt에 1추가 

if cnt.count(max(cnt)) > 1: #가장 많은 cnt가 여러개라면 물음표 출력
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))]) 