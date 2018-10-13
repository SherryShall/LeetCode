"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class TrieNode():
	def __init__(self, val):
		self.val = val
		self.isWord = False
		self.next = [None] * 26

class Trie(object):

	def __init__(self):

		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode("root")


	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		start = self.root
		for i, ch in enumerate(word):
			if not start.next[ord(ch)-97]:
				start.next[ord(ch)-97] = TrieNode(ch)
			if i == len(word)-1:
				start.next[ord(ch)-97].isWord = True
			start = start.next[ord(ch) - 97]

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		start = self.root
		for i, ch in enumerate(word):
			if not start.next[ord(ch)-97]:
				return False
			if i == len(word)-1 and (not start.next[ord(ch)-97].isWord):
				return False
			start = start.next[ord(ch)-97]
		return True

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		start = self.root
		for i, ch in enumerate(prefix):
			if not start.next[ord(ch)-97]:
				return False
			start = start.next[ord(ch)-97]
		return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)