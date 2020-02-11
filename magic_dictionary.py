#
#   https://leetcode.com/problems/implement-magic-dictionary/
#

from string import ascii_lowercase


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashes = {}

    def buildDict(self, dictonary):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.hashes = set(dictonary)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        for idx, letter in enumerate(word):
            for l in ascii_lowercase:
                if l != letter:
                    if word[:idx] + l + word[idx + 1:] in self.hashes:
                        return True
        return False


dictionary = ["a","b","ab","abc","abcabacbababdbadbfaejfoiawfjaojfaojefaowjfoawjfoawj","abcdefghijawefe","aefawoifjowajfowafjeoawjfaow","cba","cas","aaewfawi","babcda","bcd","awefj"]
f = MagicDictionary()
f.buildDict(dictionary)

inp = ["a", "b", "c", "d", "e", "f", "ab", "ba", "abc", "cba", "abb", "bb", "aa", "bbc", "abcd"]
res = [True, True, True, True, True, True, False, False, False, False, True, True, True, True, False]
f.search("abc")

for idx, w in enumerate(inp):
    assert f.search(w) is res[idx]
