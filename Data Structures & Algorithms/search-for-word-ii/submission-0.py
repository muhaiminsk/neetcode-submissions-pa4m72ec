from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Map character -> TrieNode
        self.isWord = False # Marks the end of a valid word

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]  # Go deeper
        cur.isWord = True  # Mark the end of this word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)  # Insert all words into the Trie

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # Base cases
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))  # Mark cell as visited
            node = node.children[board[r][c]]  # Move to next node
            word += board[r][c]

            if node.isWord:
                res.add(word)  # Found a valid word

            # Explore 4 directions
            dfs(r - 1, c, node, word)  # up
            dfs(r + 1, c, node, word)  # down
            dfs(r, c - 1, node, word)  # left
            dfs(r, c + 1, node, word)  # right

            visit.remove((r, c))  # Unmark cell after exploring

        # Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
