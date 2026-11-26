# Assignment 2
# Students Grade

students = {
    "s01":{"name":"Akshay", 
           "grade":87},
    "s02":{"name":"Vivek", 
           "grade":95}
}
print(students)

students["s03"] = {"name":"Uday",
                   "grade":77}
print ("Dictionary after adding new student")
print(students)

students["s01"]["grade"] = 57

print ("Dictionary after updating grade of s01 student")
print(students)

print("Prining only grades of students")
for student in students:
    print(students[student]["grade"])
    