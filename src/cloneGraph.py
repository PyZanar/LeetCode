from typing import Optional, List
import pytest

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:

        if node is None:
            return None
        
        visited = {} # コピーしたノードの記録用。キー、値ともにNode型
        
        def dfs(curr_node: Optional[Node]) -> Optional[Node]:

            if curr_node in visited:
                return visited[curr_node]
            
            cloned_node = Node(curr_node.val)
            visited[curr_node] = cloned_node

            for neighbor in curr_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        return dfs(node)
    

# グラフ生成用関数
def build_graph(adjList: Optional[List[List[int]]]) -> Optional[Node]:
    if not adjList:
        return None

    # ノードの値は1から始まるので、インデックスと合わせるために辞書を使う
    nodes = {}

    # まず全ノードを作成
    for i in range(len(adjList)):
        nodes[i + 1] = Node(i + 1)

    # 隣接関係を構築
    for i, neighbors in enumerate(adjList):
        curr_node = nodes[i + 1]
        curr_node.neighbors = [nodes[n] for n in neighbors]

    # 最初のノード（1番）を返す
    return nodes[1]


# グラフ比較用関数
def graphs_are_equal(node1, node2, visited=None):
    if visited is None:
        visited = {}

    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    if node1 in visited:
        return visited[node1] == node2

    visited[node1] = node2

    if len(node1.neighbors) != len(node2.neighbors):
        return False

    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if not graphs_are_equal(n1, n2, visited):
            return False

    return True



@pytest.mark.parametrize(
    "adjList",
    [
        ([[2,4],[1,3],[2,4],[1,3]]),
        ([[]]),
        ([])
    ]
)
def test_case(adjList):

    actual = Solution().cloneGraph(build_graph(adjList))
    expected = build_graph(adjList)

    assert graphs_are_equal(actual, expected)