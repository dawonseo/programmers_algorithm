def solution(genres, plays):
    music_dict = {i:[0, []] for i in set(genres)}
    ans = []
    
    for i in range(len(plays)):
        music_dict[genres[i]][1] += [(plays[i], i)]
        music_dict[genres[i]][0] += plays[i]

    for m in sorted(music_dict.values(), key = lambda x: -x[0]):
        if m[1]:
            if len(m[1]) == 1:
                ans += [m[1][0][1]]
            else:
                a = sorted(m[1], key = lambda x: (-x[0], x[1]))
                ans.extend([a[0][1], a[1][1]])
    
    return ans
