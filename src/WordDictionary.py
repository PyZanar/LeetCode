import pytest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root: TrieNode) -> bool:

            if j == len(word):
                return root.word

            curr = root

            if word[j] != ".":
                if curr.children.get(word[j]):
                    return dfs(j+1, curr.children[word[j]])
                return False
            else:
                for node in curr.children.values():
                    if dfs(j+1, node):
                        return True
                return False

        return dfs(0, self.root)
           
            
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
obj.addWord("bat")

print(obj.search(".at"))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)