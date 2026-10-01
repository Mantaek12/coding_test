def solution(n):
    ans = 0

    if n % 2 == 0:
        new_n = n
    elif n ==1:
        return 1
    else:
        new_n = n-1
        ans +=1

    # print(new_n)


    while new_n != 0:
        # print(new_n)
        if new_n % 2 == 0:
            new_n = new_n // 2
        else:
    
            # print(new_n)
            new_n -= 1
            ans += 1
            # print(ans)
        

        if new_n == 0 :
            return ans


if __name__ == "__main__":
    print(solution(5))
    print(solution(6))
    print(solution(5000))