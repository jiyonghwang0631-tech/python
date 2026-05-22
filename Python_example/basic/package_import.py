import test_package
from test_package import *

def package_func():
    print("이것은 패키지 함수입니다.")


def main():
    print("test_package 패키지에서 실행되는 프린트이다.")
    print(Module_a())
    print(Module_b())
    print(module_b_func())    

if __name__ == "__main__":
    main()
