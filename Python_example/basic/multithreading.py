import threading
import time

total = 0
lock = threading.Lock()

# GTL - global Interpreter Lock
# race condition 이 걸릴경우 gtl을 걸어서 안전하게 한다.
def task(name, duration):
    global total
    print(f"쓰레드 {name} 시작")
    for _ in range(1_000_000):
        with lock:
            total += 1
    time.sleep(duration)
    print(f"쓰레드 {name} {duration}초 후 완료")

def main():
    #task("first", 5)
    #task("second", 5)
    thread=[]
    for i in range(4):
        t = threading.Thread(target=task, args=(f"T{i+1}", 5 + i))
        thread.append(t)
        t.start() # 실제 함수가 실행 되는 라인
    for t in thread:
        t.join() #block
    print("main은 언제 실행 될까요?")
    print(total)
    
if __name__ == "__main__":
    main()