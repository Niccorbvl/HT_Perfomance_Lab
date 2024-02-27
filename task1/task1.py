n, m = map(int, input().split())
FirstElement = 1
FirstIteration = True
while (FirstElement != 1) or FirstIteration:
    FirstIteration = False
    print(FirstElement, end='')
    FirstElement = (FirstElement + m - 2) % n + 1
