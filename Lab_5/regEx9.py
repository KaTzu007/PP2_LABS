import re

def space(text):
    return re.sub(r"(?<!^)(?=[A-Z])", ' ', text)

text = "IAmGood"
print(space(text))