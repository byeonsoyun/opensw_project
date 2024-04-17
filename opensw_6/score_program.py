class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = english_score + c_score + python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        # 학번이 중복되는 경우 처리
        if self.search_student_by_id(student.student_id):
            print(f"이미 존재하는 학번입니다: {student.student_id}")
            return False
        self.students.append(student)
        # 등수 계산
        self.calculate_rank()
        return True

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        result = []
        for student in self.students:
            if student.name == name:
                result.append(student)
        return result

    def calculate_rank(self):
        sorted_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(sorted_students):
            student.rank = i + 1

    def sort_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_over_80(self):
        count = 0
        for student in self.students:
            if student.total_score >= 240:  # 80 * 3 = 240
                count += 1
        return count

# 입력 함수
def input_student():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    english_score = int(input("영어 점수를 입력하세요: "))
    c_score = int(input("C언어 점수를 입력하세요: "))
    python_score = int(input("파이썬 점수를 입력하세요: "))
    return Student(student_id, name, english_score, c_score, python_score)

# 출력 함수
def print_student(student):
    print(f"학번: {student.student_id}, 이름: {student.name}")
    print(f"영어: {student.english_score}, C언어: {student.c_score}, 파이썬: {student.python_score}")
    print(f"총점: {student.total_score}, 평균: {student.average_score}, 학점: {student.grade}, 등수: {student.rank}")

# 메인 함수
def main():
    grade_manager = GradeManager()
    
    # 5명의 학생 정보 입력
    print("5명의 학생 정보를 입력하세요:")
    for _ in range(5):
        student = input_student()
        grade_manager.add_student(student)

    while True:
        print("\n원하는 작업을 선택하세요:")
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 학생 탐색 (학번)")
        print("4. 학생 탐색 (이름)")
        print("5. 전체 학생 정보 출력")
        print("6. 80점 이상 학생 수 출력")
        print("7. 종료")
        choice = input("선택: ")

        if choice == '1':
            student = input_student()
            if grade_manager.add_student(student):
                print("학생이 추가되었습니다.")

        elif choice == '2':
            student_id_to_remove = input("삭제할 학생의 학번을 입력하세요: ")
            if grade_manager.remove_student(student_id_to_remove):
                print(f"{student_id_to_remove} 학생을 삭제하였습니다.")
            else:
                print(f"{student_id_to_remove} 학생을 찾을 수 없습니다.")

        elif choice == '3':
            search_student_id = input("탐색할 학생의 학번을 입력하세요: ")
            found_student = grade_manager.search_student_by_id(search_student_id)
            if found_student:
                print("학생을 찾았습니다:")
                print_student(found_student)
            else:
                print(f"{search_student_id} 학번을 가진 학생을 찾을 수 없습니다.")

        elif choice == '4':
            search_name = input("탐색할 학생의 이름을 입력하세요: ")
            found_students = grade_manager.search_student_by_name(search_name)
            if found_students:
                print("학생을 찾았습니다:")
                for student in found_students:
                    print_student(student)
                    print()
            else:
                print(f"{search_name} 이름을 가진 학생을 찾을 수 없습니다.")

        elif choice == '5':
            print("전체 학생 정보 출력")
            for student in grade_manager.students:
                print_student(student)
                print()

        elif choice == '6':
            count = grade_manager.count_students_over_80()
            print(f"80점 이상인 학생 수: {count}")

        elif choice == '7':
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 선택이 아닙니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()

