if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for v in student_marks:
        if(v == query_name):
            s = 0
            for n in student_marks.get(v):
                s = s + n
            print("{0:.2f}".format(s/len(student_marks.get(v))))
            
            

