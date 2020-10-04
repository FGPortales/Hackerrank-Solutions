if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    mi = 9999
    for v in range(len(scores)):
        if scores[v] != min(scores):
            if scores[v] < mi:
                mi = scores[v]
    n = []
    for i,v in enumerate(scores):
        if v == mi:
            n.append(names[i])

    for v in sorted(n):
        print(v)
