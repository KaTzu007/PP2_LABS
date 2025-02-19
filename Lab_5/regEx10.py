import re

def to_snake_case(text):
    return re.sub(r"(?<!^)([A-Z])", lambda match: "_" + match.group(0).lower(), text)

text = "maxSizeVolume"
print(to_snake_case(text))