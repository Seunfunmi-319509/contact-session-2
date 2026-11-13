import re

with open("baby2008.html", "r", encoding="utf-8") as file:
    content = file.read()

name_matches = re.findall(r"<td>\d+</td><td>([A-Za-z]+)</td>\s*<td>([A-Za-z]+)</td>", content)

list_of_names = []

for male_name, female_name in name_matches:
    list_of_names.append(male_name)
    list_of_names.append(female_name)


total_names = len(list_of_names)

for i in range (total_names):
    for j in range(total_names - i - 1):
        if list_of_names[j].casefold() > list_of_names[j + 1].casefold():
            list_of_names[j], list_of_names[j + 1] = list_of_names[j + 1], list_of_names[j] 

target = input("Enter the baby name you wish to search for: ").strip()

low = 0
high = len(list_of_names) - 1

while low <= high:
    mid = (low + high) // 2

    if list_of_names[mid].casefold() == target.casefold():
        print("Name found at index:", mid)
        break
    elif list_of_names[mid].casefold() > target.casefold():
        high = mid - 1
    else:
        low = mid + 1

else:
    print("Name not found!")






