list_input_a = ["52","273", "32", "스파이", "103"]

# 반복 적용
list_number=[]
for item in list_input_a:
    # 숫자로 변환
    try:
        float(item)
        list_number.append(item)
    except:
        pass
    
#출력
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다".format(list_number))