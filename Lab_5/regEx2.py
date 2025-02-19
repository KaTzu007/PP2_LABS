import re

def abb(text):
    match = re.search("abb" or "abbb", text)
    return match

text = "caabbbdfeaabb"
print(abb(text))