def read_file(filepath):
    subtitles = []
    timing = ""
    strings = []
    next_is_order_number = True
    
    with open(filepath, "r", encoding = "utf-8") as file:
        for row in file:
            if row == "\n":
                subtitles.append([timing, strings])
                timing = ""
                strings = []
                next_is_order_number = True
            elif next_is_order_number:
                next_is_order_number = False
                next_is_timing = True
            elif next_is_timing:
                next_is_timing = False
                timing = row
            else:
                strings.append(row)

    return subtitles


def write_file(filepath, subtitles):
    with open(filepath, "w", encoding = "utf-8") as file:
        for i in range(len(subtitles)):
            file.write(str(i + 1) + "\n")
            file.write(subtitles[i][0])
            for string in subtitles[i][1]:
                file.write(string)
            file.write("\n")


def move_time(string, minutes, seconds, miliseconds):
    mas = string.split(":")
    mas = list(map(int, mas[:2] + mas[2].split(",")))
    
    mas[-1] += miliseconds
    while mas[-1] >= 1000:
        mas[-1] -= 1000
        mas[-2] += 1
    while mas[-1] < 0:
        mas[-1] += 1000
        mas[-2] -= 1
    
    mas[-2] += seconds
    while mas[-2] >= 60:
        mas[-2] -= 60
        mas[-3] += 1
    while mas[-2] < 0:
        mas[-2] += 60
        mas[-3] -= 1
    
    mas[-3] += minutes
    while mas[-3] >= 60:
        mas[-3] -= 60
        mas[-4] += 1
    while mas[-3] < 0:
        mas[-3] += 60
        mas[-4] -= 1
    
    if mas[-4] < 0:  # mas[-4] is hours
        print("WRONG TIME MOVEMENT")
    
    if mas[-1] == 0:
        mas[-1] = "000"
    elif 1 <= mas[-1] <= 9:
        mas[-1] = "00" + str(mas[-1])
    elif 10 <= mas[-1] <= 99:
        mas[-1] = "0" + str(mas[-1])
    
    if mas[-2] == 0:
        mas[-2] = "00"
    elif 1 <= mas[-2] <= 9:
        mas[-2] = "0" + str(mas[-2])
    
    if mas[-3] == 0:
        mas[-3] = "00"
    elif 1 <= mas[-3] <= 9:
        mas[-3] = "0" + str(mas[-3])
    
    if mas[-4] == 0:
        mas[-4] = "00"
    elif 1 <= mas[-4] <= 9:
        mas[-4] = "0" + str(mas[-4])      
    
    return str(mas[0]) + ":" + str(mas[1]) + ":" + str(mas[2]) + "," + str(mas[3])


filepath = "movie.srt"
move_forward = False
move_minutes = 0
move_seconds = 0
move_miliseconds = 941

if not move_forward:
    move_minutes = -move_minutes
    move_seconds = -move_seconds
    move_miliseconds = -move_miliseconds

subtitles = read_file(filepath)
for i in range(len(subtitles)):
    timing = subtitles[i][0]
    timing1, timing2 = timing.split(" --> ")
    new_timing1 = move_time(timing1, move_minutes, move_seconds, move_miliseconds)
    new_timing2 = move_time(timing2, move_minutes, move_seconds, move_miliseconds)
    subtitles[i][0] = new_timing1 + " --> " + new_timing2 + "\n"
write_file("result_" + filepath, subtitles)
