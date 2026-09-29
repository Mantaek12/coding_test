# def solution(nums):
#     set_nums = len(set(nums))
#     # print(set(nums))
#     n = len(nums) / 2

#     if set_nums < n:
#         return int(set_nums)
#     else:
#         return int(n)

def solution(nums):
    return min(len(set(nums)), len(nums) // 2)


if __name__ == "__main__":
    nums1 = [3,1,2,3]
    print(solution(nums1))

    nums2 = [3,3,3,2,2,4]
    print(solution(nums2))	