# 1. print() - 출력하기
print("안녕하세요! 파이썬의 세계에 오신 걸 환영합니다.")
print("오늘은 파이썬의 기초를 배워볼 거예요.\n")

# 2. 변수와 자료형 - 값을 저장하고 쓰기
name = input("당신의 이름은 무엇인가요? ")
age = input("몇 살인가요? ")
print("반가워요,", name + "님! 당신은", age, "살이군요.")

# 변수에는 숫자도 저장할 수 있어요.
year = 2025
birth_year = year - int(age)
print("당신은", birth_year, "년에 태어났군요!\n")

# 3. 자료형의 종류
is_adult = int(age) >= 20
print("성인인가요? →", is_adult)  # 불린형: True 또는 False

height = 160.5   # 실수
hobby = "독서"   # 문자열
print("키는", height, "cm이고, 취미는", hobby, "입니다.\n")

# 4. 조건문 - 상황에 따라 다른 결과
print("당신의 나이에 따라 다른 메시지를 보여드릴게요!")
age = int(age)
if age < 10:
    print("아직 어린이네요! 코딩을 일찍 시작하다니 멋져요.")
elif age < 20:
    print("청소년이군요! 미래가 기대돼요.")
else:
    print("성인이네요! 새로운 도전을 응원합니다.")

print()  # 줄바꿈

# 5. 반복문 - 같은 동작 여러 번 하기
print("자, 이제 반복문을 이용해서 별을 5개 찍어볼게요!")
for i in range(5):
    print("★" * (i + 1))

print()

# 사용자 이름을 3번 출력해볼까요?
for i in range(3):
    print(f"{i+1}. {name}님, 파이썬 재미있죠?")

print()

# 6. 배열 (리스트) - 여러 값을 하나로
fruits = ["사과", "바나나", "딸기", "포도", "복숭아"]
print("과일 리스트:", fruits)
print("첫 번째 과일은:", fruits[0])
print("마지막 과일은:", fruits[-1])

print("\n과일을 하나씩 출력해볼게요:")
for fruit in fruits:
    print("과일:", fruit)

print()

# 리스트에 항목 추가
fruits.append("수박")
print("수박을 추가했어요! 새로운 리스트:", fruits)

# 리스트에서 항목 제거
fruits.remove("바나나")
print("바나나를 제거했어요! 현재 리스트:", fruits)

print()

# 7. 미니 프로젝트 - 내가 좋아하는 것 리스트 만들기
favorites = []
print("당신이 좋아하는 것을 3가지 입력해보세요.")
for i in range(3):
    item = input(f"{i+1}번째 좋아하는 것: ")
    favorites.append(item)

print("\n당신이 좋아하는 것들:")
for i, item in enumerate(favorites):
    print(f"{i+1}. {item}")

print("\n오늘 배운 파이썬 개념 정리 완료! 수고하셨어요 :)")
