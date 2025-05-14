# # a = [1, 2, 3, 4, 5]
# # b = a. reverse() # [5, 4, 3, 2, 1]
# # print(b) # none

# a = [1, 2, 3, 4, 5]
# b = list(reversed(a))
# print(a)
# print(b)

# c = [1, 2, 3, 4, 5]
# # sorted(리스트, reverse=bool)
# sorted(c, reverse=False) # sorted(a)
# d = list(sorted(c, reverse=True)) # 내림차순 정리
# print(d)

# 1단계
books = ["파이썬 기초", "데이터 과학 입문", "알고리즘의 이해", "머신러닝 실전", "파이썬 기초"]
print(f"1단계 - books 리스트\n{books}\n")

# 2단계
count = books.count("파이썬 기초")
print(f"\n2단계 - '파이썬 기초' 권 수 : {count}")

books.append("웹 개발의 시작")
books.insert(2, "데이터베이스 설계")

new_books = ["인공지능 개론", "클라우드 컴퓨팅"]
books.extend(new_books)
print(f"2단계 - 수정된 목록 : \n{books}\n")

# 3단계
books.remove("파이썬 기초")
last_book = books.pop()
print(f"\n3단계 - 마지막 책 : {last_book}")

books.sort()
books.reverse()
print(f"3단계 - 정렬 후 역순 목록 :\n{books}\n")

# 4단계
top_books = books[:3]
reversed_selection = books[1:5][::-1]
print(f"\n4단계 - 상위 3권 : {top_books}")
print(f"4단계 - 2~5번째 책 역순 : {reversed_selection}")

books.clear()
print(f"4단계 - 비운 목록 : {books}")