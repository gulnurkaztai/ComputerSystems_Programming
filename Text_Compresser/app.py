
import re

with open("input.txt") as file:
    content = file.read()
    words = re.findall(r"\b[a-zA-Z0-9\-]+\b", content)
    print(words)

mapped_dictionary = {}
index = 1

for word in set(words):  
    mapped_dictionary[word] = index
    index += 1


with open("output.sc", "w") as file:
    for word in words: 
        file.write(f"{mapped_dictionary[word]} ")



