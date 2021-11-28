"""
ex: {[1300, 1500], [930, 1200],[830, 845]}, 新的meeting[820, 830], return true; [1450, 1500] return false;

"""

# def can_meet(meetings, meet):
#     ((start >= meeting[0] & & start < meeting[1]) | | (end > meeting[0] & & end <= meeting[1])
#      | | (start < meeting[0] & & end > meeting[1]))
#     n_s, n_e = meet
#     for start, end in meetings:
#         if (n_e > start and n_e <= end) or (n_s >= start and n_s < end) or ( n_s < start and n_e > end):
#             return False
#     return True

#print(can_meet([[1300, 1500], [930, 1200],[830, 845]], [820, 830]))
#print(can_meet([[1300, 1500], [930, 1200],[830, 845]], [820, 850]))
#if ((meeting[0] <= start & & meeting[1] > start) | | (meeting[0] < end & & meeting[1] >= end)) return false;
import heapq
def employeeFreeTime(self, schedule):
    heap = []
    for i, v in enumerate(schedule):
        heapq.heappush(heap, (v[0].start, 0, i))

    merged_free_times = []

    while heap:
        start_time, j, i = heapq.heappop(heap)
        if not merged_free_times or merged_free_times[-1][-1] < start_time:
            merged_free_times.append([start_time, schedule[i][j].end])
        else:
            merged_free_times[-1][-1] = max(merged_free_times[-1][-1], schedule[i][j].end)

        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j + 1].start, j + 1, i))

    res = []

    for i in range(1, len(merged_free_times)):
        res.append((merged_free_times[i - 1][-1], merged_free_times[i][0]))
    return res