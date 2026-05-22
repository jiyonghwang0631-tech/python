"""
Practice 001. 이름표 출력하기

난이도: beginner
수업 순서: 001
학습 주제: 출력/문자열
관련 기본 예제: basic/a01-a07

문제:
    이름, 과정명, 날짜를 받아 3줄짜리 이름표 문자열을 만드세요.

예시:
    - ("홍길동", "Python", "2026-05-20") -> "이름: 홍길동\n과정: Python\n날짜: 2026-05-20"

작성 방법:
    1. 아래 TODO 위치에 코드를 작성합니다.
    2. 함수 이름과 반환 형식은 바꾸지 않습니다.
    3. 필요한 경우 보조 함수를 추가해도 됩니다.
"""

LEVEL = "beginner"
ORDER = 1
TOPIC = "출력/문자열"
TITLE = "이름표 출력하기"



def make_name_card(name, course, date):
    # TODO: 아래에 코드를 작성하세요.
    return f"이름: {name}\n과정: {course}\n날짜: {date}"


def main():
    card = make_name_card("홍길동", "python", "2026-05-22")
    print(card)

if __name__ == "__main__":
    main()