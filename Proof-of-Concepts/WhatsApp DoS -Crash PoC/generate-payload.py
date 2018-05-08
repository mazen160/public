#!/usr/bin/env python
text = "This text should crash your app."
for _ in range(3000):
    text += u"\u200e\u200f"

text = text.encode("utf-8")
print(text)
