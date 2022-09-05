def solution(dartResult):
    ans_list = ['', '', '']

    for i in dartResult:
        if i in [str(n) for n in range(10)]:
            dartResult = dartResult.replace(i, '+' + i)

    dartResult = dartResult.replace('+++', '+')
    dartResult = dartResult.replace('++', '+')
    dartResult = dartResult.replace('+1+0', '+10')

    rnd_list = list(dartResult.split('+'))
    rnd_list = [x for x in rnd_list if x]

    for i in range(len(rnd_list)):
        ans = ''
        for j in rnd_list[i]:
            if j in [str(n) for n in range(10)]:
                ans += '+' + j
                ans = ans.replace('+1+0', '+10')
            elif j == 'S':
                ans += "**1"
            elif j == 'D':
                ans += "**2"
            elif j == 'T':
                ans += "**3"
            elif j == '*':
                if i < 1:
                    ans += "*2"
                else:
                    ans_list[i - 1] += "*2"
                    ans += "*2"
            elif j == '#':
                ans += "*(-1)"
        ans_list[i] = ans

    sb = ''
    for i in ans_list:
        sb += i

    return eval(sb)
