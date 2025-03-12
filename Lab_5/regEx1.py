import re

def ab(text):
    match = re.search(r"a[b]*", text)
    return match

text = "cabcabbabcabagfa"
print(ab(text))