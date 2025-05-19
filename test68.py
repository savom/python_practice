#확인문제
# ㅇ낮힐수 있느 최소 사람수 2 t
t = 2
# 앉힐수 있는 최대 사람수 10 k
k = 10
#전체 100
total = 100

# 남은 사람의 수 n
# 앉힌 사람 수 m
memo = {}

def test(n,m):
    key = str([n,m])
    
    if key in memo:
        return memo[key]
    if n < 0:
        return 0
    if m ==0:
        return 1
    
    count = 0
    for i in range(t,k+1):
        count += test(n-i,i)
        
        memo[key] = count
        
        return count
    
print(test(total,t))