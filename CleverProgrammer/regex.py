import re

text = 'Random string.'

pattern = re.compile("[rdm]")

result = pattern.search(text)

print(result)