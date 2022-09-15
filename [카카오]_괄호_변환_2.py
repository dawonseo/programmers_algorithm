# 올바른 괄호 문자열인지 판별하는 함수
def is_correct(word):
    tmp = 0
    for w in word:
        if w == '(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return False
    return True


def recursive(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(w) == 0:
        return ''
    else:
        tmp = 0
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        for i in range(len(w)):
            if w[i] == '(':
                tmp += 1
            else:
                tmp -= 1

            if tmp == 0:
                u = w[:i + 1]
                v = w[i + 1:]
                break

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct(u):
        return u + recursive(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        new_word = '('
        new_word += recursive(v)
        new_word += ')'
        for s in u[1:-1]:
            if s == '(':
                new_word += ')'
            else:
                new_word += '('

        return new_word


def solution(p):
    return recursive(p)