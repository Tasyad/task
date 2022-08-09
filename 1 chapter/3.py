import re
p = re.compile(r'42\s+\w+')
text = '23 street'
text2 = '42 meaning of life'
a = p.findall(text)
b = p.findall(text2)
print(a, b)