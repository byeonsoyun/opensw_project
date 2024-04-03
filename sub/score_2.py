# 필요한 변수와 데이터 구조 초기화
students = []

# 입력 함수
def input_student():
    id = input("학번: ")
    name = input("이름: ")
    scores = {
        "영어": int(input("영어 점수: ")),
        "C언어": int(input("C언어 점수: ")),
        "파이썬": int(input("파이썬 점수: "))
    }
    student = {
        "학번": id,
        "이름": name,
        "점수": scores,
        "총점": 0,  # 계산 필요
        "평균": 0.0,  # 계산 필요
        "학점": '',  # 계산 필요
        "등수": 0  # 계산 필요
    }
    return student

# 총점/평균 계산 함수
def calculate_totals_and_averages(students):
    for student in students:
        total = sum(student['점수'].values())
        average = total / len(student['점수'])
        student['총점'] = total
        student['평균'] = average

# 학점 계산 함수
def calculate_grades(students):
    for student in students:
        if student['평균'] >= 90:
            student['학점'] = 'A'
        elif student['평균'] >= 80:
            student['학점'] = 'B'
        elif student['평균'] >= 70:
            student['학점'] = 'C'
        elif student['평균'] >= 60:
            student['학점'] = 'D'
        else:
            student['학점'] = 'F'

# 등수 계산 함수
def calculate_ranks(students):
    students.sort(key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(students):
        student['등수'] = i + 1

# 출력 함수
def print_students(students):
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("학번", "이름", "총점", "평균", "학점", "등수"))
    for student in students:
        print("{:<10} {:<10} {:<10} {:<14.2f} {:<14} {:<14}".format(student['학번'], student['이름'], student['총점'], student['평균'], student['학점'], student['등수']))

# 80점 이상 학생 수 카운트 함수
def count_students_above_80(students):
    count = sum(1 for student in students if student['평균'] >= 80)
    print(f"80점 이상인 학생 수: {count}")

# 메인 로직
def main():
    for _ in range(5):  # 5명의 학생 정보 입력 받기
        students.append(input_student())
    
    calculate_totals_and_averages(students)
    calculate_grades(students)
    calculate_ranks(students)
    
    print_students(students)
    count_students_above_80(students)

if __name__ == "__main__":
    main()
