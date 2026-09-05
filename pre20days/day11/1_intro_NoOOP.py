import random

students = []

for i in range(1, 11):
    student = {
        "name": f"student{i:02d}",
        "score": random.randint(0, 100)
    }
    students.append(student)


def show_student(student):
    print("姓名：", student["name"])
    print("分數：", student["score"])


def add_score(student, point):
    student["score"] += point
    if student["score"] > 100:
        student["score"] = 100


def is_pass(student):
    return student["score"] >= 60


def check_pass(student):
    if is_pass(student):
        print(student["name"], "及格")
    else:
        print(student["name"], "不及格")


for student in students:
    show_student(student)
    check_pass(student)
    print()

# 10 個學生，隨機產生分數，名字取名 studentXX 例： student01


class Student:
    # class 一定要有初始化的設計
    def __init__(self):
        self.name = "student"
        self.score = 100


if __name__ == "__main__":
    s1 = Student() # create Student 的實體（根據設計產生的物件）object
    # 屬性 name, score  （class 自帶的資料）
    print(s1.name)
    print(s1.score)

    s2 = Student() # create Student 的實體（根據設計產生的物件）object
    # 屬性 name, score  （class 自帶的資料）
    s2.name = "Leo"
    s2.score = 90
    print(s2.name)
    print(s2.score)

    # s1.show_info()
    # s1.add_score()


