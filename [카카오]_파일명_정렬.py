def solution(files):
    start = 0
    end = 0
    new_files = [[] for _ in range(len(files))]

    for i in range(len(files)):
        flag = 0
        for j in range(len(files[i])):
            # flag가 2일 때
            if flag == 2:
                break
            # flag가 0일 때
            elif not flag and files[i][j].isdigit():
                new_files[i].append(files[i][:j].lower())
                if files[i][j:].isdigit():
                    new_files[i].append(int(files[i][j:]))
                    new_files[i].append(i)
                    break
                else:
                    start = j
                    flag = 1
            # flag가 1일 때
            elif flag and not files[i][j].isdigit():
                end = j
                new_files[i].append(int(files[i][start:end]))
                new_files[i].append(i)
                flag = 2

    new_files.sort()

    return [files[i[2]] for i in new_files]
