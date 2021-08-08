def solution(msg):
    answer = []
    dict = {}
    for i in range(26):
        dict[chr(ord("A")+i)] = i + 1
    
    
    w = 0 
    c = 0
    
    dict_len = 26
    while(1):
        c += 1
        if(c == len(msg)):
            answer.append(dict[msg[w:c]])
            break
        elif(msg[w:c + 1] not in dict) :
            answer.append(dict[msg[w:c]])
            dict[msg[w:c+1]] = dict_len + 1
            dict_len += 1
            w = c
        
        
        
    return answer