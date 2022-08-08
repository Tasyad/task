import re
pattern = r'\s+'
text = 'Python   Exercises'
word = ''
result = re.sub(pattern, word, text)
print(result)
