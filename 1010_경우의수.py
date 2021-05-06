def factorial(num: int):
    if num <= 1:
        return 1
    else:
        return (num * factorial(num - 1))


num = int(input())
for i in range(num):
    n, m = map(int, input().split())

    answer = factorial(m) // (factorial(n) * factorial(m-n))

    print(answer)
