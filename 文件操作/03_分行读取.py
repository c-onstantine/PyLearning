file=open("./text.txt",encoding="utf-8")

while True:
    text=file.readline()
    if not text:
        break
    print(text)


file.close()