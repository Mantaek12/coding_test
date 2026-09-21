def solution(clothes):
    clothes_dict = {}
    answer = 1

    for name, category in clothes:
        # print(name, category)
        if category not in clothes_dict:
            clothes_dict[category] = 1
            # print(clothes_dict)
        else:
            clothes_dict[category ] +=1

    # print(clothes_dict)
    for count in clothes_dict.values():
        # print(count)
        count+=1
        answer *=count

    return  answer - 1

if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))  # Expected output: 5