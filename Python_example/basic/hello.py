def main():
    print("Hello World")
    print(__name__)



# if문을  쓰는 이유 import를 당했을때 __main__이 아니게 된다.
if __name__ == "__main__":
    main()
