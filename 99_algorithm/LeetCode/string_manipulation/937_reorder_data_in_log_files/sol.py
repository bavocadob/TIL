class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        letters = list()
        numbers = list()

        for log in logs:
            if log.split()[1].isdigit():
                numbers.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        result = letters + numbers
        return result
