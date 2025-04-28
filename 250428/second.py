# # 입력 구현
# a = input()

# print(a)

# """
# 입력을 몇가지 변수에 담아서
# f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요
# """

# f = input()

# print()

# # -------- 형변환 --------
# print(type(a))
# b = int(a) # 문자를 숫자로
# print(type(b))

# a = 1

# print(type(str(a)))


# -------- 문자열 고유 기능 --------
# s = 'weniv CEO licat'
# print(s.lower()) # 출력 : weniv ceo licat
# print(s.upper()) # 출력 : WENIV CEO LICAT
# print(s.find("weniv")) # 출력 : 0
# print(s.find("good")) # 출력 : -1


# s3 = "weniv-corp"
# s4, s5 = s3.split("-")
# print(s4, s5)

# '''
# 입력이 들어온다. 키 몸무게 성별 나이 이름
# 예시 180 60 남 25 김아무개
# 이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
# 이름을 f-string을 통해 세 번 반복해서 출력한다.
# '''
# print("키, 몸무게, 성별, 나이, 이름을 공백을 넣어 입력해주세요.")
# info = input()
# cm, kg, gen, age, name = info.split(" ")
# print("키 : ", cm)
# print("몸무게 : ", kg)
# print("성별 : ", gen)
# print("나이 : ", age)
# print("이름 : ", name)
# print(f"{name} "*3)

# --------- 문자열 합치기 ---------

s20 = ["modu", "labs", "good"]
print("-".join(s20))

print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name,age))
print(f'제 이름은 {name}이고, 나이는 {age}살입니다.')

print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.