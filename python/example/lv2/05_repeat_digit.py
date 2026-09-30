def solution(s):
    answer = []
    # print(s.count("1"))
    length_1 = s.count("1")
    length_2 = s.count("0")

    counter = 0

    while s != "1":
        s = bin(length_1)[2:]
        # print(new_s)
        length_2 += s.count("0")
        length_1 = s.count("1")
        counter +=1



    return [counter, length_2]

if __name__ == "__main__":
    s1 = "110010101001"	
    print(solution(s1))

    s2 = "01110"
    print(solution(s2))