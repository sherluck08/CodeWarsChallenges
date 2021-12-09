import re

def to_camel_case(text):
    matches = re.findall(r"-+\w|_+\w", text)
    for match in matches:
        text = text.replace(match, match[-1].upper())
    return text
