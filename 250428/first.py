# # 정수
# a = 10
# b = 20
# c = 0
# d = 40

# print(type(a), type(b), type(c), type(d))

# #실수
# number1 = 3.12
# number2 = -0.12
# print(type(number1), type(number2))

# #문자열
# str1 = "abcd"
# str2 = "abcd"

# str3 = '''
# 오늘은 4월 28일입니다.

# 5월이 멀지 않았네요.

# '''

# print(type(str3))
# print(str3)


# # 문자열 반복하기
# str10 = str1 * 10

# test2 = "30"

# print(str10)
# # print(str1 * test2) (x)
# print(str10 + "입니다" + "어쩌고 저쩌고")

# # 오늘은 4월 28입니다.
# a = 4
# b = 28

# #기본 방식
# print("오늘은" + a + "월 " + b + "일입니다.")

# # f-string
# # f""
# print(f"오늘은 {a}월 {b*10}일입니다.")

# # ------------- 문자열 인덱싱
# s = "life is good"
# print(s[0])
# print(s[3])

# print(s[300]) ## IndexError : string index out of range
# ## 주민등록번호가 13자리
# ## print(s[13])

# # 문자열 슬라이싱 #  [start:stop:step]
# print(s[0:3])
# print(s[0:4:2])

# # 다양한 슬라이싱 방법
# s = 'weniv CEO licat'
# print(1, s[0:5]) # 출력 : weinv
# print(2, s[6:]) # 출력 : (6번째, C부터 끝까지 출력) CEO licat
# print(3, s[:]) # 출력 : weniv CEO licat
# print(4, s[::-1]) # 출력 : 
# print(5, s[:2]) # 출력 : 

## ----------- 테스트 -----------
## ip address = 172.100.200.100
'''
1. ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다.
3. step 을 활용해서 172100200100 이 나오게 하기
'''

s = "ip address = 172.100.200.100"

# a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다.
address = s[:11]
# print(address)

ip_numbers = s[13:]
a = ip_numbers[:3]
b = ip_numbers[4:7]
c = ip_numbers[8:11]
d = ip_numbers[12:15]
# print(a, b, c, d) ## 출력 : 172 100 200 100

# 3. step 을 활용해서 172100200100 이 나오게 하기
result = ip_numbers[::1].replace('.', '')
print(result) # 출력 : 172100200100