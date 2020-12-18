def solution(begin, target, words):
    def bfs_search_words(words_dict, root):
        answer = 0
        wordsToVisit = [root]
        _wordsToVisit = []

        while True:
            answer += 1
            _wordsToVisit = []
            for word in wordsToVisit:
                if target in words_dict[word]: return answer
                else: _wordsToVisit +=  words_dict[word]
            wordsToVisit = _wordsToVisit

            if answer > len(words): return 0


    # 1. 입력으로 주어진 단어 별 변환 가능 단어 리스트 생성
    words.append(begin)
    words_dict = {}
    for word in words:
        words_dict[word] = []
        for _word in words: # 각 단어 별 연결 가능 단어 확인
            if [c1 == c2 for c1, c2 in zip(word, _word)].count(False) == 1 :
                words_dict[word].append(_word)


    # 2. BFS를 통해 가장 빨리 답을 찾을 수 있는 경우 탐색
    answer = bfs_search_words(words_dict, begin)
    return answer
