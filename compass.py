from collections import defaultdict


def filenames(names):

    d = defaultdict(int)
    out = []
    for name in names:
        #print(name, d)
        if name in d:
           d[name] += 1
           out.append(f"{name}({d[name]})")
        else:
            out.append(f"{name}")
            d[name] = 0
    return out

names = ["doc", "doc", "images", "doc(1)", "doc"]
names = ["a(1)", "a(6)", "a", "a", "a"]
print(filenames(names))
