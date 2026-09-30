# """흠.. 보자보자 일단 정렬하면 숫자가 오름차순이고.. 두 수의 곱 총 합이 최소라.. 그렇다면 정렬해서 서로 크로스 반대편 있는 것들끼리 곱하자!"""
# """정렬 + 그리디"""

def solution(A,B):
    answer = []

    new_A = sorted(A)
    new_B = sorted(B, reverse=True)

    tot = 0

    for i in range(len(new_A)):
        tot += new_A[i] * new_B[i]


    return tot

if __name__ == "__main__":
    a1 = [1, 4, 2]	
    b1 = [5, 4, 4]	
    print(solution(a1, b1))

    a2 = [1,2]	
    b2 = [3,4]	
    print(solution(a2, b2))