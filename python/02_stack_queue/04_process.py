# def solution(priorities, location):
#     answer = 0

#     queue = []

#     for i, p in enumerate(priorities):
#         queue.append((i,p))

#     # print(f"init [list] : {queue}")

#     while queue:
#         current = queue.pop(0)
#         # print(f"line11: {queue}")

#         has_higher = False

#         for item in queue:
#             # print(current[1])
#             if current[1] < item[1]:
#                 # queue.append[current]
#                 # print(queue)
#                 has_higher = True
#                 break

#         if has_higher:
#             queue.append(current)
#             # print(queue)
#         else:
#             answer +=1
#             if current[0] == location:
#                 return answer


from collections import deque

def solution(priorities, location):
    queue = []
    for i, p in enumerate(priorities):
        queue.append((i, p))

    # print(f"일반 {queue[0]}")
    queue = deque(queue)
    # print(f"데크 {queue.popleft()}")

    answer = 0
    while queue:

        current = queue.popleft()

        has_higher = any(current[1] < item[1] for item in queue)

        if has_higher:
            queue.append(current)
        else:
            answer +=1
            if current[0] == location:
                return answer



if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))  

    priorities2 = [1, 1, 9, 1, 1, 1]
    location2 = 0
    print(solution(priorities2, location2)) 