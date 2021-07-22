def solution(land):
    answer = 0
    init_max = max(land[0])
    now_index = land[0].index(init_max)
    answer += init_max
    for i in range(1, len(land)):
      tmp_max = max(land[i])
      tmp_index = land[i].index(tmp_max)
      if  (now_index == tmp_index):
        land[i][tmp_index] = 0
        tmp_max = max(land[i])
        tmp_index = land[i].index(tmp_max)
      answer += tmp_max
      now_index = tmp_index
    # print(answer)
    
    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])