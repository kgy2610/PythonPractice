import sys

class LibrarySystem:
    def __init__(self):
        self.users = {}  # 사용자 정보 저장용 딕셔너리
        ###########
        self.current_user = None # 현재 로그인 한 사용자
        ###########

        ###########
        # 도서 관리
        self.books = [] # {"title": str, "rented_by": str or None}
        ###########

    # ------------------------ 회원관리 ------------------------
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


    def login(self):  # 로그인 함수
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"✅ {username}님, 로그인 성공!✅")
            return True
        else:
            print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")
            return False

    def logout(self):
        answer = input("로그아웃 하시겠습니까? [1.네 / 2.아니요] ")
        if answer == "1":
            print("로그아웃 되었습니다.")
            self.current_user = None
            return True
        elif answer == "2":
            print("로그아웃을 취소했습니다.")
            return False
        
    # ------------------------ 도서관리 ------------------------
    def add_book(self):
        title = input("책 제목을 입력해주세요: ")
        self.books.append({"title": title, "rented_by": None})
        print(f"'{title}' 도서가 등록되었습니다.")

    def delete_book(self):
        self.show_books()
        try:
            index = int(input("삭제할 책 번호를 입력해주세요: ")) - 1
            if 0 <= index < len(self.books):
                removed = self.books.pop(index)
                print(f"'{removed['title']}' 도서가 삭제되었습니다.")
            else:
                print("존재하지 않는 책 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def show_books(self):
        print("\n[전체 도서 목록]")

        ###########
        if not self.books:
            print("📂 등록된 도서가 없습니다.")
            return
        ###########
        
        for i, book in enumerate(self.books, 1):
            status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
            print(f"{i}. {book['title']} / {status}")

    def search_books(self):
        if self.current_user is None:
            print("로그인 후 이용해주세요.")
            return
        keyword = input("검색할 책 제목 또는 키워드를 입력하세요: ").lower()
        found = False
        print("\n[검색 결과]")
        for i, book in enumerate(self.books):
            if keyword in book["title"].lower():
                status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"
                print(f"{i+1}. {book['title']} - {status}")
                found = True
        if not found:
            print("검색된 책이 없습니다.")

    # ------------------------ 대여/관리 ------------------------
    def rent_book(self):
        self.show_books()
        try:
            index = int(input("대여할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books):
                book = self.books[index]
                if book["rented_by"] is None:
                    book["rented_by"] = self.current_user
                    print(f"'{book['title']}' 책이 대여되었습니다.")
                else:
                    print("이미 대여 중인 책입니다.")
            else:
                print("존재하지 않는 책 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def return_book(self):
        user_books = [(i, b) for i, b in enumerate(self.books) if b["rented_by"] == self.current_user]
        if not user_books:
            print("반납할 책이 없습니다.")
            return
        print("[내가 대여한 책 목록]")
        for i, book in user_books:
            print(f"{i+1}. {book['title']}")
        try:
            index = int(input("반납할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books) and self.books[index]["rented_by"] == self.current_user:
                self.books[index]["rented_by"] = None
                print(f"'{self.books[index]['title']}' 책이 반납되었습니다.")
            else:
                print("해당 책은 당신이 대여한 책이 아닙니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    def extend_books(self):
        user_books = [(i, b) for i, b in enumerate(self.books) if b["rented_by"] == self.current_user]
        if not user_books:
            print("연장할 책이 없습니다.")
            return
        print("[연장 가능한 책 목록]")
        for i, book in user_books:
            print(f"{i+1}. {book['title']}")
        try:
            index = int(input("연장할 책 번호를 입력하세요: ")) - 1
            if 0 <= index < len(self.books) and self.books[index]["rented_by"] == self.current_user:
                print(f"'{self.books[index]['title']}' 연장 완료")
            else:
                print("당신이 대여한 책이 아닙니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

    # ------------------------ 메인/메뉴 ------------------------
    def menu(self):
        print("\n" + "=" * 40)
        print("[도서관 시스템 메뉴]")
        print("1. 도서 목록 보기")
        print("2. 책 추가하기")
        print("3. 책 삭제하기")
        print("4. 책 대여하기")
        print("5. 책 반납하기")
        print("6. 대여 연장하기")
        print("7. 책 검색하기")
        print("0. 로그아웃 및 종료")
        print("=" * 40)

        ###########
        try:
            choice = int(input("메뉴를 선택하세요: "))
            if 0 <= choice <= 7:
                return choice
            else:
                print("0부터 7 사이의 숫자를 입력해주세요.")
                return None
        except ValueError:
            print("숫자를 입력해주세요.")
            return None
        ###########
        # return input("메뉴를 선택하세요: ")

    def main(self):
            while True:
                choice = self.menu()
                #################
                if choice is None:
                    continue
                #################

                if choice == 1:
                    self.show_books()
                elif choice == 2:
                    self.add_book()
                elif choice == 3:
                    self.delete_book()
                elif choice == 4:
                    self.rent_book()
                elif choice == 5:
                    self.return_book()
                elif choice == 6:
                    self.extend_books()
                elif choice == 7:
                    self.search_books()
                elif choice == 0:
                    if self.logout():
                        break
                else:
                    print("잘못된 입력입니다.")

    def run(self):
        print("도서관 시스템에 오신 것을 환영합니다!")
        while True:
            print("\n1. 회원가입")
            print("2. 로그인")
            print("0. 종료")
            menu = input("메뉴를 선택하세요: ")
            if menu == "1":
                self.signup()
            elif menu == "2":
                if self.login():
                    self.main()
            elif menu == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

if __name__ == "__main__":
    system = LibrarySystem()
    system.run()