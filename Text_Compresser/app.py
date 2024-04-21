
import re

with open("input.txt") as file:
    words = re.findall(r"([a-zA-Z\-]+)", file.read())
    print(words)





