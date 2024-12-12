# Grade book program

# -------------------------
# Subprograms
# -------------------------
def read_grade_book(filename):
    file = open(filename, "r")
    for line in file:
        values = line.strip().split(",")
        grade_book.append(values)


def output_assignment():
    unit = int(input("Which unit do you want to output the results for?: "))
    for student in grade_book:
        print(student[0], student[1] + ":", student[1 + unit])
              
# -------------------------
# Main program
# -------------------------
grade_book = []
read_grade_book("gradebook.txt")
output_assignment()
