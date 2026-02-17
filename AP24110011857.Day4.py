register_number =["AP24110011857"]
data = [10, "Python", "", 25, "Loop", 40]

number_list = []
string_list = []

number_count = 0
string_count = 0
for element in data:
    if type(element) == int:
        number_list = number_list + [element]
        number_count = number_count + 1

    elif type(element) == str:
        if element != "":
            string_list = string_list + [element]
            string_count = string_count + 1
reg=register_number[0]
last_digit = int(reg[len(reg) - 1])

if last_digit % 2 == 0:
    reversed_numbers = []
    for i in range(number_count - 1, -1, -1):
        reversed_numbers = reversed_numbers + [number_list[i]]
    number_list = reversed_numbers

else:
    reversed_strings = []
    for i in range(string_count - 1, -1, -1):
        reversed_strings = reversed_strings + [string_list[i]]

    string_list = reversed_strings
print("Numbers List:", number_list)
print("Strings List:", string_list)
print("Total Numbers:", number_count)
print("Total Strings:", string_count)

