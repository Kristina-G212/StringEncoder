s = str(input())

def printGroup(char, size):
    if size != 0:
        print(char, size, sep='', end='')

group_size = 0
group_char = ''
for ch in s:
    if ch == group_char:
        group_size += 1
    else:
        printGroup(group_char, group_size)
        group_size = 1
        group_char = ch
printGroup(group_char, group_size)
