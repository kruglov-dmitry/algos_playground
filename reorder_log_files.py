from collections import defaultdict

#
#   https://leetcode.com/problems/reorder-log-files/
#


def reorder_log_files(logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        res = []

        letter_logs = defaultdict(list)
        digit_logs = []

        for entry in logs:

            idx = 0
            while entry[idx] != ' ':
                idx += 1

            if entry[idx + 1].isdigit():
                digit_logs.append(entry)
            else:
                letter_logs[entry[idx + 1:]].append((entry[:idx], entry))

        k = letter_logs.keys()
        k.sort()

        for entry in k:
            list_of_same_entries = letter_logs[entry]
            if len(list_of_same_entries) == 1:
                res.append(list_of_same_entries[0][1])
            else:
                identifiers = []
                kv = {}
                for kkk in list_of_same_entries:
                    identifiers.append(kkk[0])
                    kv[kkk[0]] = kkk[1]

                identifiers.sort()

                for kkk in identifiers:
                    res.append(kv[kkk])

        res += digit_logs

        return res


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print reorder_log_files(logs)