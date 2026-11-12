with open("name.txt", "r") as file:
    content = file.read()

names = content.split()

if len(names) == 3:
    first_name = names[0]
    middle_name = names[1]
    last_name = names[2]
    
    print(first_name + "\n" + middle_name + "\n" + last_name)

else:
    print("The file must contain your full name.")