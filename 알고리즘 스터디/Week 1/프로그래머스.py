from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = deque([0]*bridge_length)
    curWeight = 0
    truck_weights = deque(truck_weights)

    while truck_weights or curWeight > 0:
        offBridge = onBridge.popleft()            
        curWeight -= offBridge

        if truck_weights: 
            if curWeight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                onBridge.append(truck)
                curWeight += truck
            else: onBridge.append(0)
        else: onBridge.append(0)

        answer+=1

    return answer

if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))