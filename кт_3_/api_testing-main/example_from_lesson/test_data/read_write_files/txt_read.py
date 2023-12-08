from example_from_lesson.test_data.read_write_files.files import TXT_FILE


some_file = open(TXT_FILE, "r")

# print(some_file.read())
# Read the exact bites amount
# print(some_file.read(5))

# Read a single line
# print(some_file.readline())

# Get all lines as list
# print(some_file.readlines())
# print("=====")


# Read from current cursor position till the end
# print(some_file.read(5))
# print(some_file.read())

# Position cursor within the file
# some_file.seek(0)
# print(some_file.read(5))

# To open it as writable use r+
some_file.write("test")

some_file.close()
