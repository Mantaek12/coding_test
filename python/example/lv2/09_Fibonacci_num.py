def solution(n):
    answer = 0

    f0 = 0
    f1 = 1
    f_update = 0
    f = [f0, f1]

    for i in range(2, n+1):
        if i == 2:
            f.append(f0 + f1)
            # print(f)
        else:
            f.append(f[-2] + f[-1])
            # print(f)

    return f[-1] % 1234567


if __name__ == "__main__":
    n1 = 3
    print(solution(n1))

    n2 = 5
    print(solution(n2))