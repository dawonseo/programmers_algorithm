def solution(numbers, hand):
    left_hand = '*'
    right_hand = '#'
    # 순서대로 0, 2, 5, 8에 대한 거리
    keypad_dict = {1: [4, 1, 2, 3], 2: [3, 0, 1, 2], 3: [4, 1, 2, 3],
                   4: [3, 2, 1, 2], 5: [2, 1, 0, 1], 6: [3, 2, 1, 2],
                   7: [2, 3, 2, 1], 8: [1, 2, 1, 0], 9: [2, 3, 2, 1],
                   '*': [1, 4, 3, 2], 0: [0, 3, 2, 1], '#': [1, 4, 3, 2]}
    ans = ''

    for n in numbers:
        if n in [1, 4, 7]:
            ans += 'L'
            left_hand = n
        elif n in [3, 6, 9]:
            ans += 'R'
            right_hand = n
        else:
            if keypad_dict[left_hand][(n + 1) // 3] == keypad_dict[right_hand][(n + 1) // 3]:
                if hand == 'right':
                    right_hand = n
                    ans += 'R'
                else:
                    left_hand = n
                    ans += 'L'
            elif keypad_dict[left_hand][(n + 1) // 3] > keypad_dict[right_hand][(n + 1) // 3]:
                ans += 'R'
                right_hand = n
            else:
                ans += 'L'
                left_hand = n

    return ans


