#Implement a function called sort students that takes a list of student objects as input and sorts the 3 list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object 3 has the following attributes: name (string), roll number (string), and copa (float). Test the function with different input lists of students. I

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of the students in descending order of CGPA
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students


# Example usage:
students = [
  Student("Hari","A123", 7.8),
  Student("Srikanth","A124", 8.9),
  Student("Saumya", "A125", 9.1),
  Student("Mahidhar","A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {},Roll number: {}, CGPA: {}".format(student.name, student.roll_number,student.cgpa))