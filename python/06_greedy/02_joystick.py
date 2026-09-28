def solution(name):
    answer = 0
    alphabet_move = []
    name_alphabet = []
    
    for ch in name:
        idx = ord(ch) - ord('A')
        print(idx)
        alphabet_move.append(min(idx, 26-idx))
        # print(name_alphabet)
        
    n = len(name)

    cursor_move = n-1

    for i in range(n):
        # i 다음에 A가 몇 개 연속되는지 확인
        next_idx = i + 1

        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 방법 1: 오른쪽으로 갔다가 되돌아와서 왼쪽
        move1 = 2 * i + (n - next_idx)

        # 방법 2: 왼쪽으로 갔다가 되돌아와서 오른쪽
        move2 = i + 2 * (n - next_idx)

        cursor_move = min(cursor_move, move1, move2)

    return sum(alphabet_move) + cursor_move




if __name__ == "__main__":
    name1 = "JEROEN"
    print(solution(name1))

    # name2 = "JAN"
    # print(solution(name2))