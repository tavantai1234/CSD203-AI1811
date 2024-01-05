# Q1-command 1 2 and 3
from datetime import datetime
current_date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date and time: ", current_date_time)

str_current_datetime = str(current_date_time)

file_name = str_current_datetime + ".txt"
file = open(file_name, "w")
file.close()
print("File created: ", file.name)
print("-----Q2")
# Q2
with open("data.txt", "w") as file:
    file.write("Done writing" + "\nThis is new content")
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
print("--")
with open("data.txt", "w") as file:
    file.write("Opening file again..." + "\nThis is overwritten content")
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
print("--")
with open("data.txt", "w") as file:
    file.write("Name: Emma")
    file.write("\nAddress: 221 Baker Street")
    file.write("\nCity: London")

with open("data.txt", "r") as file:
    data = file.read()
    print(data)
print("-----Q3")
# Q3
with open("data.txt", "r") as file:
    data = file.readline()
    print("My first line: ", data)
    data = file.readline()
    data = file.readline()
    print("My last line: ", data)





















