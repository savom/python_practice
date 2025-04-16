dict_a = {}

dict_a['name'] = '구름'

print(dict_a)

del dict_a['name']

print(dict_a)

pets = [
    {"name" : "구름","age" : 5},
    {"name" : "초코","age" : 3},
    {"name" : "아지","age" : 1},
    {"name" : "호랑이","age" : 1},
]

print("# 우리 동네 애완 동물들")
for i in pets:
    print(i["name"], str(i["age"])+"살")
    
    
numbers = [1,2,5,6,8,3,8,2,6,4,3,2,7,9,7,8,3,2,1,1]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] =1

print(counter)

character = {
    "name": "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key,":", character[key])