# "올바른 괄호 문자열"인지 판별하는 함수
def is_correct(str):
    tmp = 0
    for i in str:
        if i == "(":
            tmp += 1
        elif i == ")":
            tmp -= 1
        if tmp < 0:
            return False
    return True


# 괄호를 뒤집어 반환하는 함수
def rev(str):
    ans = ''
    for i in str:
        if i == '(': ans += ')'
        elif i == ')': ans += '('
    return ans


def solution(p):
    # 1. 입력이 빈 문자열일 경우, 빈 문자열을 반환합니다.
    if len(p) == 0:
        return ''

    # 2. 문자열 w를 두 "균형잡인 괄호 문자열" u, v로 분리합니다.
    #   단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, 
    #   v는 빈 문자열이 될 수 있습니다.
    a = 2
    while True:
        if p[:a].count("(") == p[:a].count(")"):
            u = p[:a]
            v = p[a:]
            break
        else:
            a += 2

    # 3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if is_correct(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째로 문자로 '('를 붙입니다.
        # 4-2. 문자열 v에 대한 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고,
        #   나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        ans = '(' + solution(v) + ')' + rev(u[1:-1])
        # 4-5. 생성된 문자열을 반환합니다.
        return ans