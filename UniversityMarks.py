marks = input("Enter student marks separated by spaces: ")

marks = list(map(int, marks.split()))

# function to find average mark
def find_average_mark(marks):
  sum_of_marks = sum(marks)
  total_subjects = len(marks)
  average_marks = sum_of_marks/total_subjects
  return average_marks

# calculate grade and return it
def compute_grade(average):
    if average >= 80:
        grade = "A"

    elif average >= 60:
        grade = "B"

    elif average >= 50:
         grade = "C"

    else:
        grade = "F"
    return grade


average = find_average_mark(marks)
print("Your average marks is: ", average)

grade = compute_grade(average)
print("Your grade is: ", grade)