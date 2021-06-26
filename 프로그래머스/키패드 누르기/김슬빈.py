import copy
def solution(numbers, hand):
    numbers_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                     4: [1, 0], 5: [1, 1], 6: [1, 2],
                     7: [2, 0], 8: [2, 1], 9: [2, 2],
                                0: [3, 1]}
    left_loc = [3, 0]
    right_loc = [3, 2]

    answer = ''

    for number in numbers:
        current_loc = numbers_dict[number]

        if number in [1, 4, 7]:
            answer += "L"
            left_loc = copy.deepcopy(current_loc)
        elif number in [3, 6, 9]:
            answer += "R"
            right_loc = copy.deepcopy(current_loc)

        else:
            distance_to_left = abs(left_loc[0] - current_loc[0]) + abs(left_loc[1] - current_loc[1])
            distance_to_right = abs(right_loc[0] - current_loc[0]) + abs(right_loc[1] - current_loc[1])

            if distance_to_left  < distance_to_right:
                answer += "L"
                left_loc = copy.deepcopy(current_loc)

            elif distance_to_left > distance_to_right:
                answer += "R"
                right_loc = copy.deepcopy(current_loc)

            else:
                if hand == "left":
                    answer += "L"
                    left_loc = copy.deepcopy(current_loc)

                elif hand == "right":
                    answer += "R"
                    right_loc = copy.deepcopy(current_loc)


    return answer
