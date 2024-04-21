
import re

with open("input.txt") as file:
    words = re.findall(r"([a-zA-Z\-]+)", file.read())
    print(words)

compressed_set = {}
index = 1

for word in set(words):  
    compressed_set[word] = index
    index += 1


with open("output.sc", "w") as file:
    for word in words: 
        file.write(f"{compressed_set[word]} ")



