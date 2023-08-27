class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams_dict = {}

        for word in strs:
            sorted_word = str(sorted(list(word)))
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = list()

            anagrams_dict[sorted_word].append(word)

        result = []
        for val in anagrams_dict.values():
            result.append(val)

        return result

