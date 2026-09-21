def solution(arr):
    answer = []
    arr_len = len(arr)
    print(arr_len)
    for i in range(arr_len):
        # print(f"line5 : {i}")
        if i == arr_len - 1 or arr[i] != arr[i+1] : # 제일 끝부분일 경우 예외처리 해줘야한다.
            answer.append(arr[i])

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # Expected output: [1, 3, 0, 1]
    # print(solution([4, 4, 4, 3, 3]))        # Expected output: [4, 3]
