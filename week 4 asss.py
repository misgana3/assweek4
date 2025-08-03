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
 print("Success! 'output.txt' has been created with processed content.")


####################
def modify_file_content(input_filename, output_filename):
    try:
        #Read        
     with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify_content(e.g., convert to uppercase)
        modified_content = content.upper()

        #
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Success! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

#UserPrompt
input_file = input("Enter the name of the file to read: ")
output_file = "modified_" + input_file

#
modify_file_content(input_file, output_file)



