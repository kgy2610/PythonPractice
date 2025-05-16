class LibrarySystem:
    def __init__(self):
        self.users = {}  # 사용자 정보 저장용 딕셔너리
        self.current_user = None

    def signup(self):  # 회원가입 함수
        while True:
            username = input("아이디를 입력하세요: ")
            if username in self.users:
                print("❗ 이미 존재하는 아이디입니다.")
            else:
                break
        password = input("비밀번호를 입력하세요: ")
        self.users[username] = password
        print(f"🎉 {username}님, 회원가입이 완료되었습니다!")


    #1-2
    def login(self):  # 로그인 함수
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        if username in self.users and self.users[username] == password:
            print(f"✅ {username}님, 로그인 성공!✅")
        else:
            print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")

    def run(self):
        while True:
            print("\n===== 도서관 시스템 =====")
            print("1. 회원가입")
            print("2. 로그인")
            print("0. 종료")
            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    library = LibrarySystem()
    library.run()



# logout 기능


current_user = ["abc123"]
books = [{"title":"원피스", "rented_by":"대여가능"},{"title":"aa", "rented_by": None}]

import sys
class Library:

    # def __init__(self):
    #     self.data1 = data1

    # 1- 3
    def logout(self, current_user):
        answer = input("로그아웃 하시겠습니까? [1.네 / 2.아니요]")

        if answer == "1":
            print("로그아웃 되었습니다.")
            current_user.clear() #로그인 기능에서 추가된 변수가 확인되면 .pop(변수)로 변경
            return True # 루프 종료를 위해 True를 반환
            

        elif answer == "0":
            return False # 루프 계속 진행행

    # 2- 1
    def show_books(self, num):
        for num, title_book in enumerate(books, 1):
            print(f"{num}. {title_book["title"]} / {title_book["rented_by"]}")
            
    
lib = Library()

# 테스트

while True:
    sel = input("원하는 메뉴를 선택하세요 [1.도서목록 / 2.로그아웃 및 종료] : ")

    if sel == "1":
        lib.show_books()

    elif sel == "2":
        if lib.logout(current_user):# 반환값 받기
            break

#미니 프로젝트 
class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_title = input("책 제목을 입력해주세요: ")
        book_number = input("책 번호를 입력해주세요: ")
        self.books[book_title] = book_number
        print(f"'{book_title}' 도서가 등록되었습니다.")

    def delete_book(self):
        book_number = input("삭제할 책 번호를 입력해주세요: ")  
        title_to_delete = None

        for title, number in self.books.items():
            if book_number == number:
                title_to_delete = title
                break

        if title_to_delete:
            self.books.pop(title_to_delete)
            print("도서가 삭제되었습니다.")
        else:
            print("존재하지 않는 책 번호입니다.")

manager = BookManager()
manager.books = {"해리 포터": "758", "어린 왕자": "713"}

manager.add_book() #책 추가하기
manager.delete_book() #책 삭제하기

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.rented_by = None # 대여자(User 객체)
    
    def rent_book(self, user): # 책 대여
        if self.rented_by is None: # rented_by가 None일 때 대여가능
            self.rented_by = user # 대여자 등록
            print(f"{self.title}책이 {user.name}님께 대여되었습니다.")
            return True
        else:
            print("대여 중")
            return False

    def return_book(self, user): # 책 반납
        if self.rented_by == user: # rented_by가 사용자일 때만 반납가능
            self.rented_by = None # 반납 처리
            print(f"{self.title} 책이 반납되었습니다.")
            return True
        else:
            print("반납할 수 없습니다. 이 책은 당신이 대여한 것이 아닙니다.")
            return False

def display_books(books):
    print("\n----- 도서 목록 -----")
    for book in books:
        # 책의 대여 상태 확인하기
        if book.rented_by is None:
            # 책이 대여되지 않았다면(rented_by가 None) "대여 가능"으로 상태 설정
            status = "대여 가능"
        else:
            # 책이 대여 중이라면 누가 대여했는지 표시
            status = f"{book.rented_by.name}님이 대여 중"
        
        # 책의 정보와 상태를 출력
        print(f"ID : {book.book_id} 제목 : {book.title} 상태 : {status}")
    print("--------------------")

def display_users(users):
    print("\n----- 사용자 목록 -----")
    for user in users:
        print(f"ID : {user.user_id} 이름 : {user.name}")
    print("----------------------")

# 메인 프로그램
if __name__ == "__main__":
    # 초기 데이터 생성
    users = [
        User(1, "가"),
        User(2, "나"),
        User(3, "다")
    ]

    # 책 생성
    books = [
        Book(10, "A"),
        Book(20, "B"),
        Book(30, "C"),
        Book(40, "D")
    ]

    while True:
        print("\n----- 도서 대여 시스템 테스트 -----")
        print("1. 도서 목록 보기")
        print("2. 사용자 목록 보기")
        print("3. 도서 대여하기")
        print("4. 도서 반납하기")
        print("0. 종료")

        menu = input("\n메뉴를 선택하세요 : ")

        if menu == "1":
            display_books(books)

        elif menu == "2":
            display_users(users)
        
        elif menu == "3":
            display_users(users)
            user_id = int(input("사용자 ID를 입력하세요 : "))
            # 찾는 사용자를 저장할 변수를 None으로 초기화
            user = None
            # users 리스트를 순회하면서 일치하는 사용자 찾기
            for u in users:
                if u.user_id == user_id:
                    # 일치하는 사용자를 찾으면 user 변수에 저장
                    user = u
                    # 찾았으니까 반복문 종료
                    break
            if user is None:
                print("존재하지 않는 사용자입니다.")
                continue
            
            display_books(books)
            book_id = int(input("반납할 도서 ID를 입력하세요 : "))
            # 찾은 책을 저장할 변수를 None으로 초기화
            book = None
            # books 리스트를 하나씩 확인
            for b in books:
                # 현재 책의 book_id가 찾는 book_id와 일치하는지 확인
                if b.book_id == book_id:
                    # 일치하면 해당 책을 book 변수에 저장
                    book = b
                    # 책을 찾았으니 반복문 종료
                    break
            if book is None:
                print("존재하지 않는 도서입니다.")
                continue
            book.rent_book(user)
        
        elif menu == "4":
            display_users(users)
            user_id = int(input("사용자 ID를 입력하세요 : "))
            user = None
            for u in users:
                if u.user_id == user_id:
                    user = u
                    break
            if user is None:
                print("존재하지 않는 사용자입니다.")
                continue

            display_books(books)
            book_id = int(input("반납할 도서 ID를 입력하세요 : "))
            book = None
            for b in books:
                if b.book_id == book_id:
                    book = b
                    break
            if book is None:
                print("존재하지 않는 도서입니다.")
                continue

            book.return_book(user)

        elif menu == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택해주세요.")

class LibararySystem:
    def __init__(self):
        self.users = {} # 회원 정보, signup()으로 나중에 채우기
        self.books = [] # 도서 정보
        self.current_user = None # 로그인한 사용자 ID (str)
    
    def test_login(self, username):
        self.current_user = username
        print(f"[테스트] '{username}' 로그인 상태로 설정됨.")

    def test_books(self):
        self.books.append({"title": "파이썬 입문", "rented_by": "user"}) # 빌린 유저 임의로 추가 "user"
        self.books.append({"title": "자료구조", "rented_by": None})
        self.books.append({"title": "알고리즘", "rented_by": "user"})
        self.books.append({"title": "리눅스", "rented_by": "user"})

    def extend_books(self):
        if self.current_user is None: # 로그인 정보가 없을 때
            print("로그인 후 이용해주세요.")
            return

        # 로그인 유저의 대여한 책 조회
        users_books = [
            (i, book) for i, book in enumerate(self.books)
            if book["rented_by"] == self.current_user
        ]

        def extend_books(self):
            if self.current_user is None: # 로그인 정보가 없을 때
                print("로그인 후 이용해주세요.")
                return

        # 로그인 유저의 대여한 책 조회
        users_books = [
            (i, book) for i, book in enumerate(self.books)
            if book["rented_by"] == self.current_user
        ]

        # 대여 중인 책이 없을 때
        if not users_books:
            print("대여 중인 책이 없습니다.")
            return
        
        # 대여 중인 책이 있을 때, 목록으로 출력
        print("[대여 중인 책 목록]")
        for i, book in users_books:
            print(f"{i}. {book['title']}")

        # 연장할 책 번호 입력받기
        try:
            book_index = int(input("연장할 책 번호를 입력하세요: "))
        except ValueError: # 숫자가 아닌 문자를 입력했을 때, 오류로 걸러냄
            print("숫자를 입력해주세요.")
            return
        
        # 유효한 책 번호 검사
        if book_index < 0 or book_index >= len(self.books):
            print("존재하지 않는 책 번호입니다.")
            return
        
        # 로그인한 유저가 대여한 책인지 확인
        if self.books[book_index]["rented_by"] != self.current_user:
            print("대여한 책이 아닙니다.")
            return
        
        # 모든 조건을 만족할 때
        print(f"{self.books[book_index]['title']} 연장 완료")

# ---------------------------------------------------------------------------------

    def search_books(self) :
        if self.current_user is None: # 로그인 유저 값이 None일 때
            print("로그인 후 이용해주세요.")
            return

        if not self.books: # 등록된 도서가 없을 때
            print("도서 목록이 비어있습니다.")
            return
        
        keyword = input("검색할 책 제목 또는 키워드를 입력하세요: ").lower() # 소문자 변환(영어책)
        found = False # 검색 결과가 하나라도 있으면 True로 바뀜

        print("[검색 결과]")
        for i, book in enumerate(self.books): # 책 목록을 확인하며 제목에 키워드가 있는지 확인
            if keyword in book["title"].lower(): # 제목에 키워드가 있으면
                status = "대여 가능" if book["rented_by"] is None else f"대여중{book['rented_by']}" # status 값이 None이면 "대여 가능", 아니면 "대여중(빌린사람)"
                print(f"{i}.{book['title']} - {status}") # 책 번호. 제목 - 대여 가능 여부
                found = True # 책이 검색 되었으니 True

        if not found:
            print("검색된 책이 없습니다.") # 반복문으로 책 목록을 돌고, 일치하는 키워드가 없으면 메세지 출력

if __name__ == "__main__":
    lib = LibararySystem()
    lib.test_books()
    lib.test_login("user") ## 로그인 유저 임의로 넣기 "user"
    lib.extend_books()

    lib.extend_books()

    lib.search_books()

def menu():
    """
    사용자에게 도서관 시스템 메뉴를 출력하고 
    선택한 메뉴 번호를 반환하는 함수
    
    Returns:
        int: 사용자가 선택한 메뉴 번호 (오류 발생 시 -1 반환)
    """
    print("\n" + "=" * 40)
    print(" " * 10 + "[도서관 시스템 메뉴]")
    print("=" * 40)
    print("1. 도서 목록 보기")
    print("2. 대출 중인 도서 목록 보기")
    print("3. 책 추가하기")
    print("4. 책 삭제하기")
    print("5. 책 대여하기")
    print("6. 책 반납하기")
    print("7. 대여 연장하기")
    print("8. 원하는 도서 신청하기")
    print("9. 내 대출 목록 보기")
    print("10. 책 검색하기")
    print("0. 로그아웃 또는 종료")
    print("=" * 40)
    
    # 사용자의 메뉴 선택을 입력받음 (if문과 isdigit 메서드 활용)
    user_input = input("원하는 메뉴를 선택하세요 (0-10): ")
    if user_input.isdigit():
        choice = int(user_input)
        if 0 <= choice <= 10: # 0~10 숫자 골랐을 때
            return choice
        else: # 그 이외의 숫자 골랐을 때
            print("오류: 0부터 10까지의 숫자만 입력해주세요.")
        return -1
    else: # 숫자 이외의 문자 골랐을 때
        print("오류: 숫자만 입력해주세요.")
    return -1

def main():
    '''
    메뉴를 반복하여 출력하고 
    사용자가 종료할 때까지 프로그램을 실행합니다
    
    '''
    # 프로그램 시작 메시지 출력
    print("도서관 관리 시스템에 오신 것을 환영합니다!")
    
    while True:
        choice = menu() # 메뉴출력 및 선택 받기

        # 메뉴 선택에 따른 실행
        if choice == 0:
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다:)")
            break # 로그아웃 하면 반복문 종료

        elif choice == 1:
            print("\n도서 목록을 불러오는 중입니다...")
            # + 도서 목록 함수 불러오기?
        
        elif choice == 2:
            print("\n대출 중인 도서 목록을 불러오는 중입니다...")
            # + 대출 중인 도서 목록 함수 불러오기?

        elif choice == 3:
            print("\n새로운 책을 추가합니다...")
            # + 책 추가 함수 불러오기?

        elif choice == 4:
            print("\n책을 삭제합니다...")
            # + 책 삭제 함수 불러오기?

        elif choice == 5:
            print("\n책을 대여합니다...")
            # + 책 대여 함수 불러오기?

        elif choice == 6:
            print("\n책을 반납합니다...")
            # + 책 반납 함수 불러오기?

        elif choice == 7:
            print("\n대여 기간을 연장합니다...")
            # + 대여 연장 함수 불러오기?

        elif choice == 8:
            print("\n도서 신청을 불러옵니다...")
            # 도서 신청 함수 불러오기?

        elif choice == 9:
            print("\n내 대출 목록을 불러옵니다...")
            # 내 대출 목록 함수 불러오기?

        elif choice == 10:
            print("\n책을 검색합니다...")
            # 책 검색 함수 불러오기?

        else:
            print("\n올바른 메뉴를 선택 해주세요")