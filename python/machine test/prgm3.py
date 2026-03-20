students = [
    {"id":1, "name":"rajesh"},
    {"id":2, "name":"rahul"},
    {"id":3, "name":"sruthi"}
]

search_id = int(input("Enter student id: "))

for s in students:
    if s["id"] == search_id:
        print(f"\nStudent name: {s["name"]}\n")
        break
else:
    print("\n****Invalid student id!!****\n")