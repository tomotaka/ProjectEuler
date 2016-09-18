# -*- coding: utf-8 -*-


c_score_table = dict()
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, c in enumerate(chars):
    c_score = i + 1
    c_score_table[c] = c_score


def read_names(f):
    with open(f, 'rb') as fh:
        content = fh.read()
        names = content.split(',')
        names = [ name.replace('"', '') for name in names ]
        return names


def name_score(name):
    return sum([ c_score_table[c] for c in name ])


def main():
    names_txt = './names.txt'
    names = read_names(names_txt)

    ans = 0
    names = sorted(names)
    for i, n in enumerate(names):
        rank = i + 1
        score = rank * name_score(n)
        ans += score
        # print '%04d: %s: %d: %d' % (rank, n, name_score(n), score)
    # print '------------'
    print ans


if __name__ == '__main__':
    main()
