# and 연산
# 다른 언어에서는
# a && b

# a = True
# b = True
# c = a and b
# d = 10 > 5 and 10 < 5 # d = True and False
# f = 10 >= 10 or False # 10>=10이 True이기 때문에, 이후 모든 결과값 True

# f = False and True and True # 0 1 1
# f2 = (False or True) and True
# f3 = not((False or True)and True)

# a = 10
# b = 20
# c = a != b # 다르니? 라고 물어보는 것 # True
# d = not a != b # 다르니?라고 물어보는 것(반전) False

# # -------------- 예제1 --------------
# ### 항은 3개 이상, and/or은 마음대로 연결하여 결과 출력
# cm = int(input("키를 입력하세요 : "))
# age = int(input("나이를 입력하세요 : "))
# kg = int(input("몸무게를 입력하세요 : "))

# if(cm >= 140 and age >= 10 and kg >= 40) :
#     print("입장이 가능합니다!")
# else : 
#     print("입장이 불가능합니다.")

# # -------------- 예제2 --------------
# print("합격 조건 : [ 1개 이상 과목 100점, 평균 80점 이상]")
# k = int(input("국어점수를 입력하세요 : "))
# m = int(input("수학점수를 입력하세요 : "))
# e = int(input("영어점수를 입력하세요 : "))
# avg = (k+m+e)/3

# if(k==100 or m==100 or e==100 and avg >=80):
#     print(f"국어 : {k}점, 수학 : {m}점, 영어{e}점, 평균{avg}점으로 합격하셨습니다.")
# else:
#     print(f"국어 : {k}점, 수학 : {m}점, 영어{e}점, 평균{avg:.2f}점으로 불합격하셨습니다.")

# # -------------- 멤버연산 --------------
# st = "modulabs is good"
# sta = "good" not in st # "good"이라는 문자가 st에 없니?
# sta = "good" in st # "good"이라는 문자가 st에 있니?

# # -------------- split --------------
# a = "123456-1122335"
# c,d = a.split()
# print(c)

"""
정수 3개가 공백을 두고 입력된다.
1 2 3
합과 평균을 공백을 두고 출력한다.
평균은 소숫점 이하 셋째 자리 까지 보이게한다.
"""
a, b, c = map(int, input("정수 3개를 입력해주세요 : ").split())
sum = a + b + c
avg = sum / 3
print(f"합 : {sum}\n평균 : {avg:.3f}")