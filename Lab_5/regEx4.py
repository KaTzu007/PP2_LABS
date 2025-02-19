import re

def follow(text):
    match = re.search(r"[A-Z][a-z]+", text)
    return match

text = "sdS_skmkm Ssdf_dfw"
print(follow(text))