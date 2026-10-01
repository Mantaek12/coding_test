def solution(s):
    answer = -1

    unpair_ch = []
    # print(unpair_ch)

    for idx, ch in enumerate(s):
        # print(idx, ch)
        if unpair_ch and unpair_ch[-1] == ch:
            unpair_ch.pop()
        else:
            unpair_ch.append(ch)

    if unpair_ch == []:
        return 1
    else:
        return 0



if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))