def solution(record):
    answer = []
    dir = {}
    
    count = 1
    for i in range(len(record)) :
        tmp = record[i].split(" ")
        if(tmp[0] == "Enter") :
            dir[tmp[1]] = tmp[2]
        elif(tmp[0] == "Change") :
            dir[tmp[1]] = tmp[2]
    
    for i in range(len(record)) :
        tmp = record[i].split(" ")
        if(tmp[0] == "Enter") :
            answer.append(dir[tmp[1]]+"님이 들어왔습니다.")
            
        elif(tmp[0] == "Leave") :
            answer.append(dir[tmp[1]]+"님이 나갔습니다.")


    return answer
