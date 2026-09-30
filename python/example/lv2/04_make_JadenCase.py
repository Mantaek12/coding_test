# 처음엔 FIFO 혹은 LIFO로 생각해서 스택/큐로 생각했으나, 굳이 더 넣진 않으니까 단순 구현


def solution(s):
    answer = []

    new_s = s.split(" ")
    # print(new_s)
    for word in new_s:
        answer.append(word.upper().capitalize())

    

    return ' '.join(answer)


if __name__ == "__main__":
    s1 = "3people unFollowed me"
    print(solution(s1))

    s2 = "for the last week"	
    print(solution(s2))