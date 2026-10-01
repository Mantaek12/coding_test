def solution(brown, yellow):
    answer = []

    def get_divisor(num):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            # print(i)
            if num % i ==0:
                divisors.append((i, num // i))
        return divisors

    yellow_divisor = get_divisor(yellow)
    # print(yellow_divisor)

    while True:
        for lon, lat in yellow_divisor:
            # print(lon, lat)
            goal_lat = (lat+2) * 2
            goal_lon = lon * 2
            goal_tot = goal_lat + goal_lon

            if goal_tot == brown:
                return [lat + 2, lon + 2]



if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))