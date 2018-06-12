
class Trie:
    def __init__(self):
        self.children ={}
        self.end = False

    def allwords(self, prefix):
        l = []
        self._allwords(prefix, l)
        return l

    def _allwords(self, prefix, l):
        if self.end:
            l.append(prefix)
        for key in self.children:
            self.children[key]._allwords( prefix + key, l)

    def add(self, c):
        self.children[c] = Trie()

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.add(c)
            node = node.children[c]
        node.end = True

    def all_suffixes(self, prefix):
        node = self
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        return node.allwords(prefix)


trie = Trie()
trie.insert('foobar')
trie.insert('foo')
trie.insert('bar')
trie.insert('foob')
trie.insert('foof')

l = trie.all_suffixes('foo')

for i in l:
    print(i, end=" ")


