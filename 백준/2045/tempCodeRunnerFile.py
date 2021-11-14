for i in range(3):
        if(my_map[i].count(0) == 0):
            my_sum += sum(my_map[i])
            break

        if([my_map[i][0], my_map[i][1], my_map[i][2]].count(0) == 0):
            my_sum += sum([my_map[i][0], my_map[i][1], my_map[i][2]])
            break

    for i in range(3):
        if(my_map[i].count(0) == 1):
            my_map[i][my_map[i].index(0)] = int(my_sum - sum(my_map[i]))
        if([my_map[i][0], my_map[i][1], my_map[i][2]].count(0) == 1):
            my_map[i][[my_map[i][0], my_map[i][1], my_map[i][2]].index(0)] = int(
                my_sum - sum([my_map[i][0], my_map[i][1], my_map[i][2]]))