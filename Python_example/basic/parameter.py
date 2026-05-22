# * <- 가변 변수


def print_n_time(*value: str, n: int = 2, i: int = 4) -> str:
    """_summary_ 
    교육용 테스트 함수이다. (메시지를 전달)
    Args:
        value (str): 출력할 메세지
        n (int) : 반복 출력횟수

    returns:
        str: 에러 반환
    """
    print(type(value))
    # temp1, temp2, temp3= value
    # (temp1, temp2, temp3) = (first, second, third)
    for i in range(n):
        print(value)
        #print("first", temp1, "second", temp2, "third", temp3)
        for v in value:
            print(v, end="  ")
        print("\n\n")
    print("i의 값은:" , i)
    return "ok"

def print_keyword_argument(a, b, c, d=5, *e):
    print(a, b, c, d, e)

def main():
    return_var = print_n_time("abc", "def", "ghi", "ddd")
    #keyword_argument
    return_var = print_n_time("abc", "def", "ghi", "ddd", n=4)
    return_var = print_n_time("abc", "def", "ghi", "ddd", n=4, i=8)
    return_var = print_n_time("abc", "def", "ghi", "ddd", i=8, n=4)
    print(type(return_var))
    print(*return_var)

if __name__ == "__main__":
    main()
