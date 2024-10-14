# Teacher code program

# -------------------------
# Subprograms
# -------------------------
def tcode(teacher, numletters):
    letters = ["", ""]
    teacher = teacher.replace("'","")
    letters[0] = teacher[0]
    space = teacher.find(" ")
    letters[1] = teacher[space + 1: space + numletters]
    teacher_code = "".join(letters)
    teacher_code = teacher_code.upper()
    return teacher_code
 

# -------------------------
# Main program
# -------------------------
teacher = input("Enter the name of the teacher: ")
numletters = int(input("Enter the number of letters: "))
teacher_code = tcode(teacher, numletters)
print(teacher_code)
