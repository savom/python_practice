try:
    file = open("info.txt","w")
    # 여러 가지 처리 수행
    예외.발생해라()
    file.close()
    
except:
    print("오루가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed)