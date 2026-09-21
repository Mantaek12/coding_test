def solution(prices):
    answer = []
    price_len = len(prices)

    for i in range(price_len):
        count = 0

        for j in range(i+1, price_len):
            count += 1
            if prices[j] < prices[i]:
                break

        answer.append(count)


    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))  # Expected output: [4, 3, 1, 1, 0]