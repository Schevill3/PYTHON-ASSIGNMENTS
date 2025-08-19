# simple_file_line_read.py

try:
    # Ask user for file name
    filename = input("Enter the file name: ")

    # Open file in read mode
    with open(filename, "r") as file:
        # Create a new file name
        new_filename = "new_" + filename

        # Open new file in write mode
        with open(new_filename, "w") as new_file:
            # Read line by line and write modified version
            for line in file:
                new_file.write(line.upper())

    print("New file created:", new_filename)

except FileNotFoundError:
    print("That file does not exist.")
except Exception as e:
    print("Error:", e)
