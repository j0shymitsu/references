class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
    
    def add(self, word):
        current_trie_level = self.root
        for char in word:
            if char not in current_trie_level:
                current_trie_level[char] = {}
            current_trie_level = current_trie_level[char]
        current_trie_level[self.end_symbol] = True

    def exists(self, word):
        current_dict = self.root
        for char in word:
            if char not in current_dict:
                return False
            current_dict = current_dict[char]
        if self.end_symbol in current_dict:
            return True
        return False
    
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        letters = sorted(current_level.keys())
        for letter in letters:
            if letter != self.end_symbol:
                ext_prefix = current_prefix + letter
                next_level = current_level[letter]
                self.search_level(next_level, ext_prefix, words)
        return words
    
    def words_with_prefix(self, prefix):
        matching_words = []
        current_level = self.root
        for char in prefix:
            if char not in current_level:
                return []
            else:
                current_level = current_level[char]
            return self.search_level(current_level, prefix, matching_words)
        
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            if len(children) == 1:
                char = children[0]
                prefix += char
                current = current[char]
            else:
                break
        return prefix

    