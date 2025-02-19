import re

def aendb(text):
    match = re.search(r"a.+b$", text)
    return match

text = "sabdiib"
print(aendb(text))