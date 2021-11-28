import collections

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]

#find_mismatched_entries(badge_records)
#Expected output: ["Paul", "Curtis"], ["Martha"]


def find_mismatches(pairs):

    exit_without_entry = []
    entry_without_exit = []

    # 1 => enter -1 => exit
    # which means value of -1 is exit without entry
    # value of 2 means reentry without exit
    # remaining value of 1 is entry but no exit
    d = collections.defaultdict(int)
    for emp, badge in pairs:
        value = 1 if badge == "enter" else -1
        d[emp] += value
        if d[emp] < 0:
            exit_without_entry.append(emp)
            d[emp] = 0
        elif d[emp] > 1:
            entry_without_exit.append(emp)
            d[emp] = 1
    print(d)
    for k,v in d.items():
        if v>0:
            entry_without_exit.append(k)
    return entry_without_exit, exit_without_entry

#print(find_mismatches(badge_records))


badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",      "835"],
  ["John",      "830"],
  ["Paul",     "1315"],
  ["John",     "1615"],
  ["John",     "1640"],
  ["Paul",     "1405"],
  ["John",      "855"],
  ["John",      "930"],
  ["John",      "915"],
  ["John",      "730"],
  ["John",      "940"],
  ["Jennifer", "1335"],
  ["Jennifer",  "730"],
  ["John",     "1630"],
  ["Jennifer",    "5"]
]

from collections import defaultdict
def findSuspiciousEntry(badge_times):
    dict = defaultdict(list)
    result = defaultdict(list)
    for i, j in badge_times:
        dict[i].append(int(j))
    for k, v in dict.items():
        if len(v) >= 3:
            v.sort()
            temp = []
            print(v)
            for i in v:
                temp.append(i)
                if len(temp) >= 3:
                    if temp[-1] - temp[0] <= 100:
                        result[k] = temp[:]
                    else:
                        temp.pop(0)
    return result

#print(findSuspiciousEntry(badge_times))

from collections import defaultdict

def getMostCrowded(badgeRecords):
    badgeRecords.sort(key=lambda x: int(x[1]))
    print(badgeRecords)

    lastEnterTime = None
    crowd, res = {}, defaultdict(set)
    for person, time, action in badgeRecords:
        if action == 'enter':
            crowd[person] = None
            lastEnterTime = time
        else: # Exit
            key = tuple(crowd.keys())
            res[key].add((lastEnterTime, time))
            # To cover sub group
            for prevKey in res.keys():
                if set(prevKey).issubset(set(key)):
                    res[prevKey].add((lastEnterTime, time))
            del crowd[person]
    filteredKeys = sorted([key for key in res.keys() if len(res[key]) > 1], key=lambda k: len(k), reverse=True)
    return filteredKeys[0], res[filteredKeys[0]]

if __name__ == '__main__':
    badge_records = [
        ["Paul", "1214", "enter"],
        ["Paul", "830", "enter"],
        ["Curtis", "1100", "enter"],
        ["Paul", "903", "exit"],
        ["John", "908", "exit"],
        ["Paul", "1235", "exit"],
        ["Jennifer", "900", "exit"],
        ["Curtis", "1330", "exit"],
        ["John", "815", "enter"],
        ["Jennifer", "1217", "enter"],
        ["Curtis", "745", "enter"],
        ["John", "1230", "enter"],
        ["Jennifer", "800", "enter"],
        ["John", "1235", "exit"],
        ["Curtis", "810", "exit"],
        ["Jennifer", "1240", "exit"],
    ]
    #print(getMostCrowded(badge_records))

def badged_together(badge_records):
    crowd = set()
    res = defaultdict(set)
    badge_records.sort(key=lambda x: int(x[1]))
    #print(badge_records)
    last_entry_time = None

    for person, time, action in badge_records:
        if action == "enter":
            crowd.add(person)
            last_entry_time = time
        else:
            group = tuple(crowd)
            res[group].add((last_entry_time, time))
            # sub group
            for a_group in res.keys():
                if set(a_group).issubset(set(group)):
                    res[a_group].add((last_entry_time, time))
            crowd.remove(person)
    #print(res)
    filtered = sorted([key for key in res if len(res[key]) > 1], key=len, reverse=True)
    print(filtered[0], res[filtered[0]])


some_badge_records = [
        ["Paul", "830", "enter"],
        ["Paul", "903", "exit"],
        ["John", "908", "exit"],
        ["Jennifer", "900", "exit"],
        ["John", "815", "enter"],
        ["Curtis", "745", "enter"],
        ["Jennifer", "800", "enter"],
        ["Curtis", "810", "exit"]]

badged_together(badge_records)