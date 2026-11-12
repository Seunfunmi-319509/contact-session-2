import re

text = "My phone number is 08012345678"
result = re.findall(r"\d", text)
print(result)

text2 = "I have 3 books, 15 pens and 200 notebooks."
result2 = re.findall(r"\d+", text2)
print(result2)

text3 = "Daniel is learning Python"
result3 = re.findall(r"\w+", text3)
print(result3)

text4 = "Daniel David Esther Samuel"
result4 = re.findall(r"D\w*\b", text4)
print(result4)

text5 = "Contact us at support@gmail.com or admin@yahoo.com"
result5 = re.findall(r"\w+@\w+\.\w+", text5)
print(result5)

text6 = "My name is Oluwaseun"
result6 = re.search(r"My name is (\w+)", text6)
print(result6.group(1))

text7 = "Baby's name: Daniel"
result7 = re.search(r"Baby's name: (\w+)", text7)
print(result7.group(1))

