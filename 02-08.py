# Exam grade program

# -------------------------
# Subprograms
# -------------------------

def grade(mark):
  if mark < 2:
    return "U"
  elif mark >= 80:
    return 9
  elif mark >= 67:
    return 8
  elif mark >= 54:
    return 7
  elif mark >= 41:
    return 6
  elif mark >= 31:
    return 5
  elif mark >= 22:
    return 4
  elif mark >= 13:
    return 3
  elif mark >= 4:
    return 2
  else:
    return 1

def marks_needed(mark):
  if mark <2:
    return 2-mark
  elif mark >= 80:
    return 0
  elif mark >= 67:
    return 80-mark
  elif mark >= 54:
    return 67-mark
  elif mark >= 41:
    return 54-mark
  elif mark >= 31:
    return 41-mark
  elif mark >= 22:
    return 31-mark
  elif mark >= 13:
    return 22-mark
  elif mark >= 4:
    return 13-mark
  else:
    return 4-mark

# -------------------------
# Main program
# -------------------------

mark = int(input("Enter the mark 0-100: "))
print(f"A mark of {mark} is a grade of {grade(mark)}")
print (f"You needed {marks_needed(mark)} marks to achieve the next grade")
