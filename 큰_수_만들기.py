from collections import deque

def solution(number, k):
    number = deque(number)
    new_number = [number.popleft()]

    while len(number) >= 1:
        if not new_number:
            new_number.append(number.popleft())
        if new_number[-1] < number[0]:
            k -= 1
            new_number.pop()
            if k == 0:
                return "".join(new_number) + "".join(number)
        else:
            new_number.append(number.popleft())
            
    return ("".join(new_number) + "".join(number))[:-k]
