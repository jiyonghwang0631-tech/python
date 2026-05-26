import pickle
from pathlib import Path

from student_model import Student


def main():
    tmp = []
    path = Path(r"/home/korea_hrd_1_2/python/Python_example/basic/data/test.pickle")

    with path.open("rb") as f:
        try:
            while data := pickle.load(f):
                students.append(data)
        except EOFError:
            pass
    
    students =[]
    for stu in tmp[0]:
        students.append(stu)
    Student.print()



if __name__ == "__main__":
    main()