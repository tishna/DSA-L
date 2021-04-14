def maxRepeating(self, sequence: str, word: str) -> int:
    count = 0

    while True:
        if word * count not in sequence:
            print(word * count)
            return count -1
        count += 1
        
        
    def isSubsequence(self, s, t):
        remainder_of_t = iter(t)
        print("remainder_of_t",remainder_of_t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True
