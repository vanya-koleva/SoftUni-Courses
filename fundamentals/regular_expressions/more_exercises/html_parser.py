import re


title_pattern = r'<title>([^<>]*)<\/title>'
body_pattern = r'<body>.*<\/body>'
content_pattern = r">([^><]*)<"

text = input()

title = re.findall(title_pattern, text)
title = ''.join(title)

body = re.findall(body_pattern, text)
body = ''.join(body)

content = re.findall(content_pattern, body)
content = ''.join(content)
content = content.replace('\\n', '')

print(f"Title: {title}")
print(f"Content: {content}")
