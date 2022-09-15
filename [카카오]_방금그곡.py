def solution(m, musicinfos):
    ans_list = []

    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(",")

    for n, i in enumerate(musicinfos):
        print(i)
        play_time = (int(i[1][:2]) * 60 + int(i[1][-2:])) - (int(i[0][:2]) * 60 + int(i[0][-2:]))
        played = ""

        music_code = i[3]
        finding = m

        x = ['C#', 'D#', 'F#', 'G#', 'A#']
        y = ['H', 'I', 'J', 'K', 'L']

        for idx in range(5):
            while x[idx] in music_code: music_code = music_code.replace(x[idx], y[idx])
            while x[idx] in finding: finding = finding.replace(x[idx], y[idx])

        while len(played) < play_time:
            played += music_code

        if len(played) > play_time:
            played = played[:-(len(played) - play_time)]

        if finding in played:
            ans_list.append([play_time, n, i[2]])

    if len(ans_list):
        ans_list.sort(key=lambda x: (-x[0], x[1]))
        return ans_list[0][2]
    else:
        return "(None)"

