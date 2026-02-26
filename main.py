
with open("Input/Letters/starting_letter.txt", "r") as letter:
    with open("Input/Names/invited_names.txt", "r") as names:
        template = letter.read()
        for name in names:
            name = name.strip()
            new_letter = template.replace("[name]", f"{name}")

            with open(f"Output/ReadyToSend/letter_{name}.txt", "w") as output:
                output.write(new_letter)


