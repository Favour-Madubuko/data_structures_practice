#This is a brute force approach
def lengthOfLastWord(self, s: str) -> int:
    stripped = list(s.split()) #This returns a list of words after removing whitespaces
        
    return len(stripped[-1])