import re

def replacing(text):
    return re.sub(r"[ ,.]", ":", text)

text = " fg dffd sdf l"
print(replacing(text))