if __name__ == '__main__':
    list =[]
    scores = set()
    namelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        scores.add(score)

    second_lowest = (sorted(scores)[1])

    for i in list:
        if [i][0][1] == second_lowest:
            namelist.append(i[0])
    for j in sorted(namelist):
        print(j)
