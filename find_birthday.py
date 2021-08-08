def locate_birthday(students, name):
  check = name in students
  if check == True:
    data = students[name]
    data = data.split(" ")
    result = " ".join(data[2:len(data)])
    return result
  else:
    return False

students = {"Ajay": "Birthday is August 13, 2001", 
            "Ramesh": "Birthday is Sept 5, 2001", 
            "Umesh": "Birthday is July 9, 2002",
            "Raj": "Birthday is June 7, 2002"}
name = input("Enter the name of student:")
birthday = locate_birthday(students, name)
if birthday != False:
  print("Birthday of {} is {}".format(name, birthday))
else:
  print("Information not available")