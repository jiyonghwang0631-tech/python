class Student:
    def __init__(self, name, math, korean, english, science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

def main():
    students = [
        Student("abc", 34, 65, 35, 94),
        Student("dfg", 34, 45, 45, 50),
        Student("hij", 36, 75, 63, 94),
        Student("klm", 47, 65, 85, 70),
        Student("nop", 88, 95, 75, 33),
        Student("qrs", 64, 65, 55, 40),
        Student("tuw", 34, 25, 75, 94),
    ]

    # print(students)
    # print(students[0])
    print("이름\t 국어\t 수학\t 영어\t 과학\t")
    for student in students:
        print(f"{student.name}\t {student.korean}\t {student.math}\t {student.english}\t {student.science}")



if __name__ == "__main__":
    main()
