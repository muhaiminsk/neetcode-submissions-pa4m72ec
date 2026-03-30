class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei= collections.defaultdict(list)#f

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word [j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])#f
        q = deque([beginWord]) #f
        res= 1 #forgot

        while q:
            for i in range(len(q)): #f
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord) #f
            res += 1
        return 0


