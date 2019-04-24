#
#   https://leetcode.com/problems/word-break/
#
#   Given a string and dictionary determine if string can be segmented into
#   a space-separated sequence of one or more dictionary words.
#

#
#   Approach based on dynamic programming.
#   Faster than initial and less verbose in terms of LOC:
#   1. find all words from dict that are present within string
#   2. scan all substrings from [0:i] -> [0:len] to check whether they can be decoded as word from dict
#   3. the last entry will contain result for the whole word
#

def word_break_v2(s, wordDict):
    sz = len(s)

    w_in_str = set()
    for w in wordDict:
        if w in s:
            w_in_str.add(w)

    dp = [False for _ in range(sz + 1)]
    dp[0] = True

    for i in range(1, sz + 1):
        for w in w_in_str:
            if s[i - len(w):i] == w:
                dp[i] = dp[i] or dp[i - len(w)]
                if dp[i]:
                    break
    return dp[sz]


#
#   Initial approach - not too bad in terms of performance
#   But based on heuristic from tests to use better strategy depend on input
#

def word_break_v1(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def another_word_break(ss, wordDict):
            l = len(ss)

            if l == 0:
                return True

            s = ss

            only_whitespaces = True
            for l in ss:
                if l != ' ':
                    only_whitespaces = False
                    break

            if only_whitespaces:
                return True

            for w in wordDict:
                start_idx = None
                try:
                    start_idx = s.index(w)
                except:
                    pass

                if start_idx is not None:
                    new_str = s.replace(w, ' ')
                    if another_word_break(new_str, wordDict):
                        return True

            return False

        def word_break(s, wordDict):
            start_idx = 0
            end_idx = 1
            l = len(s)

            if end_idx > l:
                return True

            res = False
            while end_idx != l + 1:
                cur_word = s[start_idx:end_idx]
                if cur_word in wordDict:
                    if word_break(s[end_idx:], wordDict):
                    return True
                end_idx += 1

            return res

        #
        # Check should we dive into processing or there some letter are missing at all?
        #

        dct = {}
        for l in s:
            dct[l] = dct.get(l, 0) + 1
        for l in dct:
            present = False
            for w in wordDict:
                if l in w:
                    present = True
                    break
            if not present:
                return False

        #
        #   Nono, Magic number emperically choosen to use different approach for processing
        #

        if len(wordDict) > 20:
            return word_break(s, wordDict)
        else:
            return another_word_break(s, wordDict)