def gradingStudents(grades):
    arr = []
    for v in grades:
        if v < 38:
            arr.append(v)
        elif (v//10)*10+5-v < 0:
            if (v//10)*10+10-v < 3:
                arr.append((v//10)*10+10)
            else:
                arr.append(v)
        else:
            if (v//10)*10+5-v < 3:
                arr.append((v//10)*10+5)
            else:
                arr.append(v)
    return arr

grades_count= int(input())
grades = [int(input()) for v in range(grades_count)]

result = gradingStudents(grades)

for v in result:
    print(v)