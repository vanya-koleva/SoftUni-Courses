from bs4 import BeautifulSoup

html_string = input()

soup = BeautifulSoup(html_string, features="html.parser")

title = soup.title.text.strip()

for tag in soup(["script", "style"]):
    tag.extract()

content = soup.body.get_text()
content = content.replace('\\n', "")

print(f"Title: {title}")
print(f"Content: {content}")
