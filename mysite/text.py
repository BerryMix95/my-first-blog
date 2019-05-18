class Text:
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class:" + self.text

t = Text("hi")
print(t)
print(t.text)
