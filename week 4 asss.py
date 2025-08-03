



#
 open("input.txt", "w") as infile:
    infile.write("The sun rises in the east.\n")
    infile.write("Birds sing in the morning.\n")
    infile.write("Coffee smells amazing today.\n")
    infile.write("Let's start the day with energy.\n")
    infile.write("Python makes automation fun!\n")

#
    open("input.txt", "r") as infile:
    content = infile.read()

word_count = len(content.split())

uppercase_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(uppercase_content)
    outfile.write(f"\n\nWORD COUNT: {word_count}\n")
print("✅ Success! 'output.txt' has been created with processed content.")
