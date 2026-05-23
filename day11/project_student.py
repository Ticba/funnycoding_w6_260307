import random


class Student:
    def __init__(self, number):                 # 初始化 method (function)，建構子
        self.name = f"student{number:02d}"
        self.score = random.randint(0, 100)     # attribute （內建變數/內建資料）

    def show_student(self):                     # method （內建 function）
        print("姓名：", self.name)
        print("分數：", self.score)

    def add_score(self, point):
        self.score += point

        if self.score > 100:
            self.score = 100

    def _is_pass(self):
        return self.score >= 60

    def check_pass(self):
        if self._is_pass():
            print(self.name, "及格")
        else:
            print(self.name, "不及格")

students = []

for i in range(1, 11):
    students.append(Student(i))


students[0].show_student()
students[0].add_score(10)
students[0].show_student()
students[0].check_pass()

print()

students[1].show_student()
students[1].add_score(5)
students[1].show_student()
students[1].check_pass()


print(students[0] == students[1])


# 物件導向 Object Oriented Programming


# 樹梅派
# c++
# coding （程序安排）
# 打包成 class（？