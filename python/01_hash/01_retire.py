# def solution(participant, completion):
#     answer = 0

#     count = {}

#     for name in participant:
#         if name in count:
#             count[name] += 1
            
#         else:
#             count[name] = 1

#     for name in completion:
#         count[name] -=1

#     for name, value in count.items():
#         if value == 1:
#             return name

from collections import Counter

def solution(participant, completion):
    answer = 0

    count = Counter(participant)
    # print(count)
    for name in completion:
        count[name] -= 1

    for name, value in count.items():
        if value == 1:
            return name

if __name__ == "__main__":
    participant1 = ["leo", "kiki", "eden"]	
    completion1 = ["eden", "kiki"]
    print(solution(participant1, completion1))

    participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]	
    completion2 = ["josipa", "filipa", "marina", "nikola"]
    print(solution(participant2, completion2))

    participant3 =    ["mislav", "stanko", "mislav", "ana"]	
    completion3 = ["stanko", "ana", "mislav"]	
    print(solution(participant3, completion3))