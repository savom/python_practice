import random
print("# random 모듈")

# random() : 0.0 <= x <1.0 사이의 float 리턴
print("- random():",random.random())

# uniform(min,max): 지정한 범위 사이의 float 리턴
print("- uniform(10,20):", random.uniform(10,20))

# randrange(): 지정한 범위의 int를 리턴
# - randrange(max): 0 부터 max 사이의 값을 리턴
# - randrange(min,max): min부터 max 사이의 값을 리턴
print("- randrange(10):",random.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜텀하게 선택
print("- choice([1,2,3,4,5])", random.choice([1,2,3,4,5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞기
print("- shuffle([1,2,3,4,5])",random.shuffle([1,2,3,4,5]))

# sample(list, k = <숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print("- sample([1,2,3,4,5], k=2):" , random.sample([1,2,3,4,5],k=2))