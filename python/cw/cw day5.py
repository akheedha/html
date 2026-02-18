python = {"alice", "bob", "charlie"}
dataScience =  {"Monk", "jack", "rahul"}

python.add("ramu")
dataScience.remove("Monk")

courses = python.intersection(dataScience)

print(f"Students in both courses are: \n {courses}")

only_python = python.difference(dataScience)
print(f"Students in python are: \n {only_python}")

all_students = python.union(dataScience)
print(f"All students are : \n {all_students}")

course_count = {
    "python" : len(python),
    "dataScience" : len(dataScience),
}

for course, count in course_count.items():
    print(f"course: {course}, Student: {count}")

growth_projection = {
    course: count*2 for course, count in course_count.items()
}

print("Growth projection ",growth_projection)