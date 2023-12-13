class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        anagram_match = [name for name in word_list if sorted(self.word) == sorted(name)]
        return anagram_match


