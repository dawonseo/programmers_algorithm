def solution(s):
    my_list = list(s[2:-2].split('},{'))
    ans = []

    for i in range(len(my_list)):
        my_list[i] = list(map(int, my_list[i].split(',')))

    my_list.sort(key=len)

    for i in my_list:
        for j in i:
            if j not in ans:
                ans.append(j)
                break

    return ans