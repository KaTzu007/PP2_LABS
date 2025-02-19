import re

def lower(text):
    match = re.search(r"[a-z]+_[a-z]+", text)
    return match

text = "ACD_wds abs_cdz"
print(lower(text))