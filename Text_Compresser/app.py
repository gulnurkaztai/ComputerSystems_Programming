
import re
# import os
# print("Current Working Directory:", os.getcwd())

with open("./Text_Compresser/input.txt") as file:
    content = file.read()
    words = re.findall(r"\b[a-zA-Z0-9\-]+\b", content)
    # print(words)

mapped_dictionary = {}
index = 1

for word in set(words):  
    mapped_dictionary[word] = index
    index += 1


with open("output.sc", "w") as file:
    for word in words: 
        file.write(f"{mapped_dictionary[word]} ")


with open("output.sc", "r") as compressed_file:
    indices = compressed_file.read()

# print("--------------------------------")
# print(mapped_dictionary.items())

reversed_dictionary = {index: word for word, index in mapped_dictionary.items()}
# print(reversed_dictionary)

with open("output.sc", "r") as file:
    indices = file.read().split()

for index in indices:
    word = reversed_dictionary[int(index)]
    print(word)

