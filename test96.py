def write_text_file(filename,text):
    try:
        file = open(filename,"w")
        return
        file.write(text)
    except:
        print("오류가 발생했습니다")
    finally:
        file.close()
        
write_text_file("test.txt","안녕하세요!")
    