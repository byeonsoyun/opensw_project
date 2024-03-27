NUM_STUDENTS = 5
NUM_SUBJECTS = 3

class Student:
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores
        self.total_score = sum(scores)
        self.average = self.total_score / NUM_SUBJECTS
        self.grade = ''
        self.rank = 0

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

def input_students():
    students = []
    for _ in range(NUM_STUDENTS):
        id = input("학번: ")
        name = input("이름: ")
        scores = [int(input(f"{subject}: ")) for subject in ["영어", "C-언어", "파이썬"]]
        students.append(Student(id, name, scores))
    return students

def calculate_ranks(students):
    sorted_students = sorted(students, key=lambda student: student.total_score, reverse=True)
    for i, student in enumerate(sorted_students):
        student.rank = i + 1

def print_students(students):
    print("성적관리 프로그램")
    print("=" *105)  # 구분선의 길이를 늘림
    print("{:<15}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
        "학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수"))  # 이름 열의 너비 조정
    print("=" * 105)  # 구분선의 길이를 늘림
    for student in students:
        print("{:<16}{:<10}{:<13}{:<11}{:<12}{:<10}{:<12.2f}{:<10}{:<12}".format(
            student.id, student.name, *student.scores, student.total_score, student.average, student.grade, student.rank))
    print("=" * 105)  # 구분선의 길이를 늘림

def main():
    students = input_students()
    for student in students:
        student.calculate_grade()
    calculate_ranks(students)
    print_students(students)

if __name__ == "__main__":
    main()

