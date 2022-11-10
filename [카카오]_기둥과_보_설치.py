def solution(n, build_frame):
    def building(arr):
        for x, y, a in arr:
            # 기둥
            if a == 0:
                if y == 0:
                    continue
                elif [x, y-1, 0] in ans_list:
                    continue
                elif [x, y, 1] in ans_list:
                    continue
                elif [x-1, y, 1] in ans_list:
                    continue
                else:
                    return False
            # 보
            else:
                if [x, y-1, 0] in ans_list:
                    continue
                elif [x+1, y-1, 0] in ans_list:
                    continue
                elif [x-1, y, 1] in ans_list and [x+1, y, 1] in ans_list:
                    continue
                else:
                    return False
        return True
    
    ans_list = []
    
    # a가 타입, b가 삭제/설치
    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            ans_list.append([x, y, a])
            if not building(ans_list):
                ans_list.remove([x, y, a])
        # 삭제
        else:
            ans_list.remove([x, y, a])
            if not building(ans_list):
                ans_list.append([x, y, a])
    
    ans_list.sort()
    
    return ans_list
    
