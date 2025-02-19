import re

def toCamelCase(text):
    text = text.lower()
    parts = text.split('_')
    camel = ''.join(word.capitalize() for word in parts[1:])
    string = parts[0] + camel
    return re.sub(r"[A-z]+_[A-z]+", string, text)

text = "MAX_SIZE_Volume"
print(toCamelCase(text))