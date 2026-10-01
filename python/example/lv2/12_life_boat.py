def solution(people, limit):
    answer = 0

    sorted_people = sorted(people, reverse=True)
    # print(sorted_people)
    light = len(sorted_people) - 1
    heavy = 0

    while heavy <= light:
        if sorted_people[heavy] + sorted_people[light] <= limit:
            heavy += 1
            light -=1
            print(heavy)
        else: 
            heavy +=1
            print("here")


    return heavy

if __name__ == "__main__":
    solution([70, 50, 80, 50], 100)
    solution([70, 80, 50], 100)