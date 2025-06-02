try:
    #숫자 변환
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    #출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:",2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)