import os
import re


def sort_by_integer_pattern(l, pattern):
    t = []
    for i in l:
        m = re.match(pattern, i)
        if m is not None:
            t.append((int(m.group(1)), i))
    return sorted(t)


def markdown_table(head, data):
    C = len(head)
    R = len(data[0])
    text = '|' + '|'.join(head) + '|  \n' + '|-' * C + '|  \n'
    for r in range(R):
        text += ('|{}' * C + '|  \n').format(*[data[c][r] for c in range(C)])
    return text
