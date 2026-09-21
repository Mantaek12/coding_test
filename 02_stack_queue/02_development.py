from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []

    for p, s in zip(progresses, speeds):
        # print(p, s)
        days.append(ceil((100-p)/s))

    # print(days)
    release_day = days[0]
    count = 1

    for i in range(1, len(days)):
        # print(i)
        if release_day >= days[i]:
            count += 1
        else:
            answer.append(count)
            release_day = days[i]
            count = 1
        # print(count)
    answer.append(count)

    return answer


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))                  # Expected output: [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # Expected output: [1, 3, 2]
