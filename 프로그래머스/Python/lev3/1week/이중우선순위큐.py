import heapq
def solution(operations):
    heap = []
    max_heap = []
    for oper in operations:
        current = oper.split()
        if current[0] =="I":
            num = int(current[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-1 * num, num))
        else:
            if len(heap) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            else:
                min_value = heapq.heappop(heap)
                max_heap.remove((-1*min_value, min_value))
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    return [0,0]