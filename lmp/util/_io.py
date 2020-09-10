import os
import re


def sort_by_integer_pattern(l, pattern):
    t = []
    for i in l:
        m = re.match(pattern, i)
        if m is not None:
            t.append((int(m.group(1)), i))
    return [i for _, i in sorted(t)]


def limited_ckpts(folder, limit, patterns):
    fs = os.listdir(folder)
    for pattern in patterns:
        for i in sort_by_integer_pattern(fs, pattern)[:-limit]:
            os.remove(os.path.join(folder, i))
