
def main():
    path = r"/home/korea_hrd_1_2/python/Python_example/basic/data"
    # f = open(path + "\\text.txt" "w")
    # f.write("Hello Python Programming...!")
    # f.close()
    with open(path + "/text.txt", "w") as f:
        f.write("hello!")
    

if __name__ == "__main__":
    main()
