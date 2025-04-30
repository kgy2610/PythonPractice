# a = "good"
# b = "a" in a
# print(len(a))

# x = [1, 2, 3]
# y = ['apple', 'banana', 'cherry']
# t = ['a', ['c', 'd'], 'c']
# z = [1, [2], 3] in [2] # a in b -> b 안에 a가 있나?
# ## -> true가 되려면, [2] 안에 [1, [2], 3]가 존재해야한다


t3 = [5, 4, 3, [2, 1]]
t4 = []
t4.append(1)
print(4)

t4.append(2) # append는 리스트 뒤에 붙인다.
t4.clear() # 리스트 안 데이터 삭제
t4.remove(3) # 리스트 안에서 특정 값을 찾아 지운다.
t4 = [5, 4, 3, 2, 1] # 오름차순 정렬
t4. sort() # 권장 x
print(t4)

# 리스트 만들 때 방법
a = []
b = list()

t4.pop()