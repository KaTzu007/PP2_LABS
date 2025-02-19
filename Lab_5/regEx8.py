import re

def splitUp(text):
    parts = re.split(r"(?<!^)(?=[A-Z])", text)
    return parts

text = "asfAsjnSdnjDHFLddhrn"
print(splitUp(text))