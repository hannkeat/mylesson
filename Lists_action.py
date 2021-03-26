if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        # print(lists)
        action = input().split()

        if action[0] == 'insert':
            print(lists)
            print(lists[1:])
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
            # print(lists, sep="\n")
            pass


"""
sample input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


"""
