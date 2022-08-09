import re
p = re.compile(r'[^localhost:8888/].+')
text = 'localhost:8888/ilovepython'
a = p.findall(text)
print(a)