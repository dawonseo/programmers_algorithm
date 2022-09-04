def solution(s):
    num_li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, val in enumerate(num_li):
        s = s.replace(val, str(idx))

    return int(s)