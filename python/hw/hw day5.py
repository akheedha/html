frontend = {'Anjana','Anjali','Sunnu','Ramu'}
backend = {'Kailas', 'Sachu','Anjana'}

backend.add('Suttu')
frontend.remove('Anjali')

print(f"\nStudents in both courses {frontend & backend}")
print(f"Students only in backend {backend - frontend}")
print(f"Students who are unique {backend ^ frontend}\n")

courses = {}
courses['frontend'] = len(frontend)
courses['backend'] = len(backend)

for x,y in courses.items():
    print(f"Number of students in {x} is: {y}")
    
print("")

fullstack = {'student_count': courses['frontend'] + courses['backend']}
print(f"Total students = {fullstack['student_count']}\n")
