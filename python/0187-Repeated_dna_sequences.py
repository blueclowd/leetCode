'''
Description:
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
'''


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = defaultdict(int)

        for i in range(len(s) - 9):
            sub_s = s[i:i + 10]

            table[sub_s] += 1

        return [sub_s for sub_s, frequency in table.items() if frequency > 1]
