if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        # print(lists)
        action = input().split()

        if action[0] == 'insert':
            lists.insert(int(action[1]), int(action[2]))

        elif action[0] == 'remove':
            lists.remove(int(action[1]))

        elif action[0] == 'append':
            lists.append(int(action[1]))

        elif action[0] == 'sort':
            lists.sort()

        elif action[0] == 'pop':
            lists.pop()

        elif action[0] == 'reverse':
            lists.reverse()

        elif action[0] == 'print':
            print(lists, sep="\n")



