import datetime


def main():
    list_a = [1,2,3]
    list_b = [4,5,6]
    # return 결과를 수정
    print(list_a + list_b)
    # elephant sign(:=) : 기존에는 값을 변수에 넣고, 다음 줄에서 사용해야 했는데
    # := 를 사용하면 값을 저장하면서 동시에 표현식 안에서 사용할 수 있다.
    print(list_a := list_a.__add__(list_b))
    # list 자체를 수정
    list_a.extend(list_b)
    print(list_a)

    # * 연산
    print(list_a * 4)
    print(list_a.__mul__(4))

    # append
    list_b.append("추가 원소")  #type : ignore
    print(list_b)

    # insert
    list_b.insert(3, 7)
    print(list_b)

    #삭제
    print(list_b.pop())
    print(list_b)
    print(list_b.pop(0))
    print(list_b)
    list_b.remove(6)
    print(list_b)
    print(list_b.index(7))
    list_b = ["a", "b", "c", "d", "e", "f"]
    list_e = [*str("hwang ji yong")]
    print(list_b.index("e"))
    print(list_e)
    print(list_e.__len__())
    print(len(list_e))

    print("K" in list_e)
    print("g" in list_e)

    del list_e[4]
    print(list_e)
    ptime = datetime.datetime.now()
    list_e.append(ptime)
    print(list_e[16])
    del list_e[16]
    del ptime
    print(list_e)


if __name__ == "__main__":
    main()
