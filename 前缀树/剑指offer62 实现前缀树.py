class TrieNode(object):
    def __init__(self):
        self.end = False
        self.nexts = [None]*26

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if word == None:
            return
        cur = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if cur.nexts[index] == None:
              cur.nexts[index] = TrieNode()
            cur = cur.nexts[index]
        cur.end = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word == None:
            return False
        cur = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if cur.nexts[index] == None:
                return False
            cur = cur.nexts[index]
        if cur.end == True:  # 易错点
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix == None:
            return False
        cur = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if cur.nexts[index] == None:
                return False
            cur = cur.nexts[index]
        return True
