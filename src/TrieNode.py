class TrieNode:

    def __init__(self):
        self.end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):

            if j == len(word):
                if root.end:
                    return True
                else:
                    return False

            curr = root
            if curr.children.get(word[j]):
                return dfs(j + 1, curr.children.get(word[j]))
            else:
                return False

        return dfs(0, self.root)

    def startsWith(self, prefix: str) -> bool:
        def dfs(j, root):

            if j == len(prefix):
                return True

            curr = root
            if curr.children.get(prefix[j]):
                return dfs(j + 1, curr.children.get(prefix[j]))
            else:
                return False

        return dfs(0, self.root)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
