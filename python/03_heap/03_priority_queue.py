import heapq

def solution(operations):
    answer = []
    # print(operations)
    heap = []
    for operation in operations:
        cmd, value = operation.split()
        # print(cmd)
        value = int(value)
        if cmd == "I":
            
            heapq.heappush(heap, value)
            # print(heap)
        elif cmd == "D":
            if not heap:
                continue
            if value == -1:
                heapq.heappop(heap)
            elif value == 1:
                max_value = max(heap)
                # print(max_value)
                heap.remove(max_value)
                heapq.heapify(heap)

    if heap:
        max_value = max(heap)
        min_value = heap[0]
        answer = [max_value, min_value]
    else:
        answer = [0, 0]
    

    return answer



if __name__ == "__main__":
    test_cases = [
    {
        "operations": [
            "I 16",
            "I -5643",
            "D -1",
            "D 1",
            "D 1",
            "I 123",
            "D -1"
        ],
        "expected": [0, 0]
    },
    # {
    #     "operations": [
    #         "I -45",
    #         "I 653",
    #         "D 1",
    #         "I -642",
    #         "I 45",
    #         "I 97",
    #         "D 1",
    #         "D -1",
    #         "I 333"
    #     ],
    #     "expected": [333, -45]
    # }
]

for test_case in test_cases:
    result = solution(test_case["operations"])

    print("입력:", test_case["operations"])
    print("출력:", result)
    print("예상:", test_case["expected"])
    print()
