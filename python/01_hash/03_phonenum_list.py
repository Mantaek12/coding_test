def solution(phone_book):

    hash_map ={}

    for nums in phone_book:
        hash_map[nums] = 1

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if arr in hash_map and arr != nums:
                return False

    return True


    # return 0

if __name__ == "__main__":
    phone_book1 = ["119", "97674223", "1195524421"]	
    print(solution(phone_book1))

    # phone_book2 = ["123","456","789"]	
    # print(solution(phone_book2))

    # phone_book3 = ["12","123","1235","567","88"]	
    # print(solution(phone_book3))