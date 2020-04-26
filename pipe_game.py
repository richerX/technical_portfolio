def pipesGame(state):
    
    '''
    <posihing matrix>
    <find all source points>
    for source_point in source_points:
            <find start points>
            for start_point in start_points:
                    <initialize current points>
                    while current_points:
                            new_current_points = []
                            for current_point in current_points:
                                    for adjacent_point in moves(current_point, current_value):
                                            <analyze adjacent point>
                                            <control the leakage>
                                            <control timings>
                                            <control found_final_value>
                            current_points = new_current_points
    <check global_leakage>
    <compute final answer by timings>
    '''
    
    #  generate 0 border around matrix
    zeros_array = [0 for _ in range(len(state[0]) + 2)]
    matrix = [zeros_array]
    for string in state:
        array = [0]
        for elem in string:
            try:
                array.append(int(elem))
            except:
                array.append(elem)
        array.append(0)
        matrix.append(array)
    matrix.append(zeros_array)    
    water = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    #  find source points
    source_points = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if ord("a") <= ord(str(matrix[i][j])) <= ord("z"):
                source_points.append((i, j))
    
    #  emulating the game
    leakage_time = None
    global_leakage = False
    for source_point in source_points:
        source_value = matrix[source_point[0]][source_point[1]]
        final_value = chr(ord(source_value) + ord("A") - ord("a"))
    
        # find start points
        start_points = []
        adjacent_cells = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in adjacent_cells:
            adjacent_point = (source_point[0] + dx, source_point[1] + dy)
            adjacent_value = matrix[adjacent_point[0]][adjacent_point[1]]
            if source_point in moves(adjacent_point, adjacent_value):
                start_points.append(adjacent_point)
        
        # running through start points
        found_final_value = True
        for start_point in start_points:
            start_value = matrix[start_point[0]][start_point[1]]
            current_time = 1
            found_final_value = False
            visited = {source_point, start_point}
            
            # initialize current_points
            if start_value == 7 and start_point[0] == source_point[0]:  # left-right
                current_points = [[start_point, 8]]
            elif start_value == 7 and start_point[1] == source_point[1]:  # up-down
                current_points = [[start_point, 9]]
            else:
                current_points = [[start_point, start_value]]
            water[start_point[0]][start_point[1]] = current_time
            
            # run, water, run
            while current_points:
                current_time += 1
                new_current_points = []
                for point in current_points:
                    current_point = point[0]
                    current_value = point[1]
                    for adjacent_point in moves(current_point, current_value):
                        adjacent_value = matrix[adjacent_point[0]][adjacent_point[1]]
                        if adjacent_point in visited:
                            pass
                        elif ord("a") <= ord(str(adjacent_value)) <= ord("z"):
                            pass
                        elif ord("A") <= ord(str(adjacent_value)) <= ord("Z") and adjacent_value == final_value:
                            found_final_value = True                            
                        elif current_point in moves(adjacent_point, adjacent_value):
                            if adjacent_value == 7 and adjacent_point[0] == current_point[0]:  # left-right
                                new_current_points.append([adjacent_point, 8])
                            elif adjacent_value == 7 and adjacent_point[1] == current_point[1]:  # up-down
                                new_current_points.append([adjacent_point, 9])
                            else:
                                new_current_points.append([adjacent_point, adjacent_value])
                            previous_time = water[adjacent_point[0]][adjacent_point[1]]
                            if previous_time == 0 or current_time < previous_time:
                                water[adjacent_point[0]][adjacent_point[1]] = current_time
                        elif leakage_time is None or current_time < leakage_time:
                            leakage_time = current_time
                            global_leakage = True
                        visited.add(adjacent_point)   
                current_points = new_current_points
            if not found_final_value:
                global_leakage = True
    
    # computing answer
    if global_leakage:
        sign = -1
    else:
        sign = 1
        leakage_time = 10 ** 9
    return sign * sum([sum([1 * (leakage_time > elem > 0) for elem in array]) for array in water])


# point = (i, j), value = matrix[i][j]
def moves(point, value):
    up, down, right, left = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if value == 1:
        moves_array = [up, down]
    elif value == 2:
        moves_array = [left, right]
    elif value == 3:
        moves_array = [down, right]
    elif value == 4:
        moves_array = [left, down]
    elif value == 5:
        moves_array = [left, up]
    elif value == 6:
        moves_array = [up, right]
    elif value == 7:
        moves_array = [left, right, up, down]
    elif value == 8:
        moves_array = [left,right]
    elif value == 9:
        moves_array = [up, down]
    else:
        return []
    return [(point[0] + dx, point[1] + dy) for dx, dy in moves_array]
