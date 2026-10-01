def solution(n):
    answer = 0
    num = bin(n).count("1")
    # print(num)

    i = 1

    while True:
        if bin(answer).count("1") == num:
            return answer
        else:
            answer = n + i
            
            i +=1
        
    
  

if __name__ == "__main__":
    n1 = 78
    print(solution(n1))

    n2 = 15
    print(solution(n2))