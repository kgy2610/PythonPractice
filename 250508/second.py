# c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]

# """
# 1. good이라는 문자열을 인덱싱 기법으로 추출
# 2. 슬라이싱 기법을 통해 [123, "good"]을 추출출
# """
# print(c[2], c[4][3][1])
# print(c[4][3][0:2])

# 데이터 삭제 (리스트 안 데이터만 삭제)
# li = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]
# li.clear()
# print(li)

# b = [1, 2, 3]

# """
# 빈리스트를 만든다.
# append를 사용하여 이중 리스트를 만든다.
# 출력한다.
# 리스트의 데이터를 다 지운다.
# 출력한다.
# copy를 활용한다.
# 카피를 활용한 리스트에 append를 사용하여 출력한다.
# """
# li = []
# li.append([1, 2, 3])
# print(f"이중 리스트 : {li}")
# li.clear()
# print(f"데이터를 지운 리스트 : {li}")
# Clist = li.copy()
# Clist.append([4, 5, 6])
# print(f"카피 후 append 리스트 : {Clist}")

# count
a = [1, 2, 3, "okay", 1, 1, 1]
print(a.count(1)) # 4

b = [1, 2, 3, [1, 2, 3, 1]]
print(b.count(1))