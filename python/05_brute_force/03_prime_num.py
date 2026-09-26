from itertools import permutations

def solution(numbers):
    answer = 0
    nums = set()

    prime = False
    

    for i in range(1, len(numbers) +1):     # numbers에서 몇가지 숫자를 조합할지 결정하는 반복문
        for p in permutations(numbers, i):  # 주어진 numbers에서 i가지 숫자로 조합
            # print(p)
            num = int(''.join(p))
            # print(num)
            nums.add(num)
            # print(list(nums))

    for k in nums:
        k = int(k)
        # print(k)
        prime_list = []
        if k < 2 :
            continue

        for j in range(2, int(k**0.5)+1):
            
            if k % j == 0:
                prime_list.append(False)
            else:
                prime_list.append(True)

        if False not in prime_list:
            answer +=1



    return answer


if __name__ == "__main__":
    num1 = "17"
    num2 = "011"
    print(f"num1 = {solution(num1)}")
    print(f"num2 = {solution(num2)}")