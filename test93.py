try:
    #파일열기
    file=open("info.txt","w")
    예외.발생해라
except:
    print("오류가 발생했습니다.")
    
finally:
    file.close()
    
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)