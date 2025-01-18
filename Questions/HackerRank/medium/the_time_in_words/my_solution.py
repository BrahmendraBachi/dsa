import os


def number_to_words(number):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number < 10:
        return units[number]
    elif 10 <= number < 20:
        return teens[number - 10]
    else:
        return tens[number // 10] + ("-" + units[number % 10] if number % 10 != 0 else "")


# Example usage:
inp_number = 17
text_representation = number_to_words(inp_number)
print(text_representation)


def timeInWords(h, m):
    h_word = (number_to_words(h)).replace("-", " ")
    new_h_word = (number_to_words(h + 1)).replace("-", " ")
    m_word = ""
    new_m_word = ""
    if m > 0:
        m_word = (number_to_words(m)).replace("-", " ")
        new_m_word = (number_to_words(60 - m)).replace("-", " ")
    if m == 0:
        return f"{h_word} o' clock"
    elif m == 1:
        return f"one minute past {h_word}"
    elif m == 15:
        return f"quarter past {h_word}"
    elif m == 30:
        return f"half past {h_word}"
    elif 1 < m < 30:
        return f"{m_word} minutes past {h_word}"
    elif m == 45:
        return f"quarter to {new_h_word}"
    elif 30 < m < 60:
        return f"{new_m_word} minutes to {new_h_word}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inp_h = int(input().strip())
    inp_m = int(input().strip())
    result = timeInWords(inp_h, inp_m)
    fptr.write(result + '\n')
    fptr.close()
