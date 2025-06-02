try:
    #파일열기
    file = open("info.txt","w")
    # 여러가지 처리 수행
    # 파일 닫기
    file.close()
except:
    print("오류가 발생했습니다.")
    
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.cloes:", file.close)
    