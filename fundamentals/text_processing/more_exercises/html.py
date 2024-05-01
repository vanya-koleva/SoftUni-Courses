title = input()
article = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {article}\n</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n    {comment}\n</div>")
