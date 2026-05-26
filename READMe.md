PYTHON
======

## 2025-5-21

Anaconda (conda) ->  가상환경      

1. dependency (의존성)  -> 프로젝트 마다 라이브러리 관리 *(파이썬라이브러리)
    `.venv/` => 프로젝트 마다 라이브러리 관리 <br>
    .venv를 만들어도 root의 바이너리를 만들어서 사용한다.

> ! conda로 가상환경을 만들어도 커널은 공유한다 커널까지 가상화를 위해서 WSL 같은 것을 사용한다.

>커널 상위의 가상환경 => VM 머신


2. C와 비교
    " C " 
    1. main() 필수, main 아래 및 라인
    2. 컴파일 언어 (전처리 -> 어셈블리어 -> 바이너리 기계어) (코드완성 전제)



    "python" 
    1. built in variable이 있다. (인터렉티브 셀로 실행)
    2. 인터프리터(C프로그램) 언어 (한줄씩 해석) Cpython(C파이썬)
    3. ;이 없다 , 라인을 맞춰야 하나의 블럭으로 처리 된다.
        indentation(띄어쓰기)


동적 타이핑
type -> int [A] (정적타입) -> int
런타임 도중 변한다 
*파이썬에서는 primitime type 이 없다 type -> class(c++, 구조체 함수)

Frame(프레임) <-(변수 scope) 
and(파이썬) 키워드 == &&(c언어)
async ~ await (비동기(같이 사용)) 여러게 쓰레드를 사용할때 키워드만 사용.
(c는 응용 해야만 사용 가능)
def (함수를 정할때) , C는 -> 타입 + 식별자()
del (객체를 삭제 할때) free랑 같이 사용
except (예외 처리) try ~ except ~ final 같이 사용 
import (소스불러올때) import ~ from 같이 사용 (C는 #include)
lamda (간단한 함수 사용) (c에서 inline)
yield (generateor 함수 할 때 사용)

str() -> 컨테이너()
indexing, slicing == c (arry 문법)


## 2025-5-22
함수, 함수 정의, 함수 호출, 매개변수, 반환값 설명
kwargs, args 설명
list 설명, list 예제
list method 설명, list method 예제
ractice 문제 1~10 연습
module, package 설명, import 문법 설명


## 2025 - 5 - 26
class , method , special method 설명(dunder method)
instance method, class 변수, property 설명
상속과 다중 상속
