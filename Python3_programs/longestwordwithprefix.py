class TNode():
    def __init__(self, end=0, strn=''):
        self.end = end
        self.childs = [None for i in range(26)]
        self.strng = strn


class Solution:

    def add(self, root, st, i, l):
        if i == l:
            return

        if root.childs[ord(st[i]) - ord('a')] is None:
            val = (0, 1)[i == (len(st) - 1)]
            strng = ("", st)[i == (len(st) - 1)]
            root.childs[ord(st[i]) - ord('a')] = TNode(val, strng)

        else:
            root.childs[ord(st[i]) - ord('a')].end = (root.childs[ord(st[i]) - ord('a')].end, 1)[i == (len(st) - 1)]
            root.childs[ord(st[i]) - ord('a')].strng = (root.childs[ord(st[i]) - ord('a')].strng, st)[i == (len(st) - 1)]

        self.add(root.childs[ord(st[i]) - ord('a')], st, i + 1, l)

    def get_long_word(self, root):
        if not any([True for i in root.childs if i and i.end]):
            self.ans = (self.ans, root.strng)[len(root.strng) > len(self.ans)]
            return

        for i in root.childs:
            if i == None or i.end == 0:
                continue

            self.get_long_word(i)

    def longestWord(self, words):
        self.length = 0
        self.ans = ""

        root = TNode()

        for st in words:
            self.add(root, st, 0, len(st))

        self.get_long_word(root)

        return self.ans



s=Solution()

print(s.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))


    # ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))
