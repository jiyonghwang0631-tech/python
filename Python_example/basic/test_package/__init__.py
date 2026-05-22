from module_a import Module_a, module_a_func, module_var_a 
from module_b import Module_b, module_b_func, module_var_b


__all__ = ["module_var_a", "module_var_b", "module_a_func"]

def package_func():
    print("이것은 패키지 함수입니다.")

print("test_package 패키지에서 실향되는 프린트이다. ")
