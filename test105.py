import sys

# 명령 매개변수 출력
print(sys.argv)
print("---")

print("getwindowsversion:()",sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:",sys.version)

sys.exit()