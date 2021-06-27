def solution(n):
    answer = []
    tmp_arr = [[0] * n for _ in range(n)]
    flag = 0
    count = 1
    while(n>0):
      for i in range(n):
        if(flag%3 ==0):
          tmp_arr[i + flag//3 +flag//3][flag//3] = count
        elif(flag%3 == 1):
          tmp_arr[- ((flag//3) + 1)][i + (flag//3 + 1)] = count
        elif(flag%3 == 2):
          tmp_arr[- ((flag//3) + 1 + (i+1))][- ((flag//3)  + flag//3 + 1 + (i+1))] = count
        count += 1
      flag += 1
      n -= 1
    for i in range(len(tmp_arr)):
      answer += (tmp_arr[i][:i+1])
    return answer

solution(5)