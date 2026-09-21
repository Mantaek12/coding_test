
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    current_weight = 0
    while len(truck_weights) > 0:
        time +=1
        current_weight = current_weight - bridge.pop(0)

        # print(f"현재 무게 : {current_weight}")

        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    time += bridge_length
    return(time)
    



if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))          # Expected output: 8
    print(solution(100, 100, [10]))               # Expected output: 101
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # Expected output: 110
