def letterCombinations(self, digits: str) -> List[str]:
    return self.getAllCombinations(digits)


def getAllCombinations(self, digits, pos_str=""):
    keyboard = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if digits == "":
        return [] if pos_str == "" else [pos_str]
    digit = digits[0]
    all_combs = []
    digit_letters = keyboard[digit]
    for letter in digit_letters:
        all_combs = all_combs + self.getAllCombinations(digits[1:], pos_str + letter)
    return all_combs
