import os


def gradingStudents(grades):
    # Write your code her
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            diff = 5 - (grade % 5)
            if diff < 3:
                rounded_grades.append(grade + diff)
            else:
                rounded_grades.append(grade)
    return rounded_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades_inp = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades_inp.append(grades_item)

    result = gradingStudents(grades_inp)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
