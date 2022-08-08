import re
pattern = r'^0'
text = input('Enter your phone number: ')
word = '+996'
result = re.sub(pattern, word, text)
print(result)

