
Example Usage 2
student_info = {
    'age': 21,
    'address': "Cairo",
    'id': 101,
    'phone_number': "0123456789",
    'per_email': "aly@gmail.com",
    'bus_email': "aly@univ.edu",
    'faculty': "Engineering",
    'enrollment_date': "2021-09-01",
    'begin_date': "2021-09-15",
    'password': "mypassword"
}

internship = Internship(student_info, "Google", "Software Eng", "3 months")
print(internship.apply_internship("Aly"))
print(internship.apply_internship(["Bob", "joe", "Alice"]))