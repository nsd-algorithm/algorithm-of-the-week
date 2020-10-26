from collections import defaultdict
import copy
visit = []
def bfs_graph(tickets,graph,queue):
    global visit

    while(queue):
        n, path = queue.pop(0)
        if(len(path) - 1 == len(tickets)):
            #print(path)
            visit.append(path)
            return
        else:
            for next in graph[n]:
                tmp_graph = copy.deepcopy(graph)
                #재귀 때문에 계속 쓸 임시 그래프 만듬
                queue.append((next,path + [next]))
                tmp_graph[n].remove(next)
                #방문한 티켓 삭제
                bfs_graph(tickets,tmp_graph,queue)



def solution(tickets):
    graph = defaultdict(list)
    tmp = []
    for i in tickets:
        graph[i[0]].append(i[1])
    lentmp = len(tmp)
    for k in graph.keys():
        graph[k].sort()
    start = "ICN"
    queue = [(start,[start])]
    bfs_graph(tickets,graph,queue)
    #print("answer",visit)
    visit.sort()
    return visit[0]
#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
