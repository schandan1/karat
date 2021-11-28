import bisect

logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

from collections import OrderedDict


def part1():
    logs1.sort(key=lambda x:int(x[0]))
    print(logs1)

    d = OrderedDict()
    r = OrderedDict()
    for time, user, resource in logs1:
        time = int(time)
        if user in d:
            d[user].append(time)
        else:
            d[user] = [time]
        if resource in r:
            r[resource].append(time)
        else:
            r[resource] = [time]
    print(d)
    print(r)

    for k,v in r.items():
        for t in v:
            i = bisect.bisect_right(v, t+300)
            print("FOR Resouece ", k, " current time ", t, " index for 5 mins ", t+300 , " is ", i)


def upper_bound(arr, target):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high)//2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    print("For target ", target, " index is ", low)
    return low

#print(upper_bound([53651, 53760, 54001, 54060, 54359], 54060))
import heapq
from collections import defaultdict

def most_requested_resource(logs):
    """
    given logs, return most requested resource under 5 minutes,
    along with its access count
    :param logs:
    :return:
    """
    resources = defaultdict(list)
    max_resource_access = 0
    max_resource_name = ''
    logs.sort(key=lambda x: (x[2], int(x[0])))
    for time, user, resource in logs:
        time = int(time)

        while resources[resource] and time - resources[resource][0] > 300:
            heapq.heappop(resources[resource])

        heapq.heappush(resources[resource], time)
        # calculate max resource by checking the length of the heap
        max_resource_access_new = max(
            max_resource_access, len(resources[resource]))
        if max_resource_access_new != max_resource_access:
            max_resource_name = resource
            max_resource_access = max_resource_access_new

    return max_resource_name, max_resource_access


print(most_requested_resource(logs1))

logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]
print(most_requested_resource(logs2))
#https://leetcode.com/discuss/interview-question/1392828/Indeed-Karat-Interview

