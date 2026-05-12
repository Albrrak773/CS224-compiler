import re

input_file = open("file.exp", "r", encoding="utf-8")
input_text_raw = input_file.read()
input_text_raw = input_text_raw.replace(" ", "").replace("\n", "")
input_text = re.split(r"(\W+)", input_text_raw)
print(f"Input: {input_text}")
input_index = 0
tokenval = 0


def lexan():
    global input_index, input_text
    if input_index < len(input_text):
        t = input_text[input_index]
        input_index += 1
        if t.isdigit():
            global tokenval
            tokenval = int(t)
            return "NUM"
        return t
    else:
        return "EOF"
