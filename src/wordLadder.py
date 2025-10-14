from typing import List
from collections import defaultdict, deque
import pytest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # wordDictを作成
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                wordDict[pattern].append(word)


        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for adjWord in wordDict[pattern]:
                    if not adjWord in visited:
                        visited.add(adjWord)
                        queue.append((adjWord, step+1))

        return 0

@pytest.mark.parametrize(
    "beginWord, endWord, wordList, expected",
    [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
    ]
)
def test_case(beginWord, endWord, wordList, expected):
    sol = Solution()
    actual = sol.ladderLength(beginWord, endWord, wordList)
    assert actual == expected